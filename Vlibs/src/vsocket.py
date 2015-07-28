
import thread, time

from socket import socket, AF_INET, SOCK_DGRAM

from vpacket import vPacket
from vaddress import vAddress
from vusuario import vUsuario

from vconstantes import ACAO_confirmarPacote, MAX_SEQUENCE, LIMIT_PKT_POR_SEG

PROTOCOLO = '!xxv1n3rxx!'

class vSocket(socket):

    def __init__(self):
        
        socket.__init__(self, AF_INET, SOCK_DGRAM)            
        
        self.__pacotes_recebidos_lk = thread.allocate_lock()    
        self.__pacotes_recebidos    = []
        
        self.__pacotes_confirmar_lk = thread.allocate_lock()
        self.__pacotes_confirmar    = {}
        
        self.__vusuarios_lk = thread.allocate_lock()
        self.__vusuarios    = {}
        
        self.ALLOWED = 0
        self.DENIED  = 1
        self.PASSED  = 2            
        
    
    def remove_vusuario(self, key_addr):
        self.__vusuarios_lk.acquire()        
        if self.__vusuarios.has_key(key_addr):            
            del self.__vusuarios[key_addr]            
        self.__vusuarios_lk.release() 
        
        self.__pacotes_confirmar_lk.acquire()
        if self.__pacotes_confirmar.has_key(key_addr):
            del self.__pacotes_confirmar[key_addr]
        self.__pacotes_confirmar_lk.release()
    
    def get_pacotes_confirmar_lk(self): 
        return self.__pacotes_confirmar_lk
    
    def get_pacotes_perdidos(self):
        pkts = self.__pacotes_confirmar.copy()
        pkts_perdidos = []
        
        for k in pkts:            
            for s in pkts[k]:
                if pkts[k][s].get_time()+1 < time.time():
                    pkts_perdidos.append(pkts[k][s])
                    del self.__pacotes_confirmar[k]
                    
        return pkts_perdidos                     
    
    def add_pacotes_recebidos(self, pacote):
        self.__pacotes_recebidos_lk.acquire()
        self.__pacotes_recebidos.append(pacote)
        self.__pacotes_recebidos_lk.release()    
    
    def clear_pacotes_recebidos(self):
        self.__pacotes_recebidos_lk.acquire()
        pacotes_recebidos = self.__pacotes_recebidos
        self.__pacotes_recebidos = []
        self.__pacotes_recebidos_lk.release()
        
        return pacotes_recebidos    
    
    def add_pacotes_confirmar(self, pacote):
        self.__pacotes_confirmar_lk.acquire()
        addr = str(pacote.get_endereco().get_key_addr())
        sequ = str(pacote.sequencia)            
                         
        if self.__pacotes_confirmar.has_key(addr):
            dic_pacotes_confirmar = self.__pacotes_confirmar.get(addr)            
            dic_pacotes_confirmar.update({sequ: pacote})            
        else:
            self.__pacotes_confirmar.update({addr: {sequ: pacote}})            
        self.__pacotes_confirmar_lk.release()        
    
    def clear_pacotes_confirmar(self, pacote):
        self.__pacotes_confirmar_lk.acquire()
        retorno = False
        
        addr = str(pacote.get_endereco().get_key_addr())
        sequ = pacote.get_arg(0)            
                
        if self.__pacotes_confirmar.has_key(addr):                                            
            del self.__pacotes_confirmar[addr][sequ]
            
            if len(self.__pacotes_confirmar[addr]) == 0:
                del self.__pacotes_confirmar[addr]
                
            retorno = True
        self.__pacotes_confirmar_lk.release()                
        
        return retorno 
    
    def __calcula_sequencial(self, address):
        
        key_addr = address.get_key_addr()        
        retorno  = None
        
        self.__vusuarios_lk.acquire()
        
        obj_vusuario = self.__recupera_cria_vusuario(key_addr)            
            
        obj_vusuario.sq_ultimo_pacote_enviado = obj_vusuario.sq_ultimo_pacote_enviado+1
        if obj_vusuario.sq_ultimo_pacote_enviado == MAX_SEQUENCE:
            obj_vusuario.sq_ultimo_pacote_enviado = 1
        
        obj_vusuario.tm_ultimo_pacote_enviado = time.time()
        
        retorno = obj_vusuario.sq_ultimo_pacote_enviado
        
        self.__vusuarios_lk.release()
        
        return retorno    
    
    def __recupera_cria_vusuario(self, key_addr):
        
        obj_vusuario = None
        
        if self.__vusuarios.has_key(key_addr):
            obj_vusuario = self.__vusuarios[key_addr]
        else:            
            obj_vusuario = vUsuario()
            self.__vusuarios.update({key_addr:obj_vusuario})
        
        return obj_vusuario
    
    def recupera_vusuario(self, key_addr = None):
        obj_vusuarios = None
        
        if key_addr and self.__vusuarios.has_key(key_addr):
            obj_vusuarios = self.__vusuarios[key_addr]
        else:
            obj_vusuarios = self.__vusuarios
            
        return obj_vusuarios
        
    
    def controle_fluxo(self, pacote):
        
        key_addr = pacote.get_endereco().get_key_addr()
        retorno  = None 
                
        self.__vusuarios_lk.acquire()
        
        obj_vusuario = self.__recupera_cria_vusuario(key_addr)
        
        obj_vusuario.QTD_PCK_RECV_POR_SEG += 1
        
        if time.time() > obj_vusuario.TIME_PRIMEIRO_PCK_RECV:
            obj_vusuario.TIME_PRIMEIRO_PCK_RECV = time.time()+1
            obj_vusuario.QTD_PCK_RECV_POR_SEG   = 1
                
        if obj_vusuario.QTD_PCK_RECV_POR_SEG <= LIMIT_PKT_POR_SEG: 
        
            s1 = pacote.get_sequencia()
            s2 = obj_vusuario.sq_ultimo_pacote_recebido
            
            if ( s1 > s2 ) and ( s1 - s2 <= MAX_SEQUENCE/2 ) or ( s2 > s1 ) and ( s2 - s1 > MAX_SEQUENCE/2 ):
                obj_vusuario.sq_ultimo_pacote_recebido = s1;
                obj_vusuario.tm_ultimo_pacote_recebido = pacote.get_time()
                retorno = self.ALLOWED
            else:
                retorno = self.PASSED
                
        else:
            retorno = self.DENIED
        
        self.__vusuarios_lk.release()
        
        return retorno
     
    def envia_pacote(self, address, tipo, acao, args = []):
        
        sequence = self.__calcula_sequencial(address)
        
        pacote = vPacket(address, PROTOCOLO, sequence, tipo, acao, args)                                    
        
        if tipo == 0:
            self.add_pacotes_confirmar(pacote)
        
        data = pacote.get_data()
        addr = address.get_addr()
        
        print "Env - %s" % data
        
        self.sendto(data, addr) 
    
    def recebe_pacote(self, buffer = 1024):
        
        data, addr = self.recvfrom(buffer)
                    
        #print "Recv - %s" % data
        
        endreco = vAddress(addr)
        pacote  = vPacket.instancia_vPacote(data, endreco)
        
        if pacote.get_protocolo() == PROTOCOLO:
            
            #Se tipo for igual a 0 envia a confirmacao
            if pacote.get_tipo() == 0:
                sequence = str(pacote.get_sequencia())
                self.envia_pacote(endreco, 1, ACAO_confirmarPacote, [sequence])                                    
                                        
        else:
            pacote = None                
        
        return pacote