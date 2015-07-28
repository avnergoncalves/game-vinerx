'''
Created on 15/03/2011

@author: avner.goncalves
'''
from Configs.config import HOST, PORTA

from vsocket import vSocket
from vaddress import vAddress

class VinerOnline(vSocket):
    '''
    VinerOnline
    '''

    def __init__(self):
        '''
        Constructor
        '''
        vSocket.__init__(self)
        
        #self.setblocking(False)
        
        self.CONECTADO = 1
        self.ESPERANDO = 2
        self.DESCONECT = 3
        self.ERROLOGIN = 4          
        
        self.__addr_server = vAddress(HOST, PORTA)            
        
        self.__obj_usuario_dic = {}
        
        self.key = False
        
        self.flg_conectado = self.DESCONECT
        
    def get_vusuario_server(self):
        key_addr = self.__addr_server.get_key_addr()        
        return self.recupera_vusuario(key_addr)
    
    def get_addr_server(self):
        return self.__addr_server
    
    def get_obj_usuario_dic(self):
        return self.__obj_usuario_dic;    
    
    def busca_usuario_por_key(self, k):
        retorno = None
        
        if self.__obj_usuario_dic.has_key(k):
            retorno = self.__obj_usuario_dic[k];
            
        return retorno
    
    def is_conectado(self):
        return (self.flg_conectado == self.CONECTADO)
    
    def remove_usuario(self, key):
        if self.__obj_usuario_dic.has_key(key):
            self.__obj_usuario_dic.pop(key)
    
    def registra_usuario(self, obj_usuario):
        if not self.__obj_usuario_dic.has_key(obj_usuario.key):
            self.__obj_usuario_dic.update({obj_usuario.key:obj_usuario})
    
    def conectar_servidor(self, login, senha, tentativas = 5): 
        if self.flg_conectado != self.CONECTADO:                                   
            self.envia_pacote_server(1, 1, [login, senha])
            self.flg_conectado = self.ESPERANDO            

    def disconnect_server(self):
        if self.is_conectado():            
            self.__conectado = False    
    
    def envia_pacote_server(self, tipo, acao, args = []):
        self.envia_pacote(self.get_addr_server(), tipo, acao, args)
        