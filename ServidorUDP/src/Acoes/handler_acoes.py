'''
Created on 29/04/2011

@author: avner.goncalves
'''
from vconstantes import ACAO_SERVER_desconectar, ACAO_CLIENT_desconectar
class HandlerAcoes(object):
    
    def __init__(self):
        self.acoes_privadas = {}
        self.acoes_publicas = {}        
     
    def set_acoes_privadas(self, key, acao):
        self.acoes_privadas.update({key:acao})
    
    def set_acoes_publicas(self, key, acao):
        self.acoes_publicas.update({key:acao})
    
    def show_acoes(self):
        
        print 'Acoes Privadas'
        for key in self.acoes_privadas:
            print 'Comando: [%s] Acao: %s \n' % (key, self.acoes_privadas[key])
            
        print 'Acoes Prublicas'
        for key in self.acoes_publicas:
            print 'Comando: [%s] Acao: %s \n' % (key, self.acoes_publicas[key])
        
    def execute_acao(self, pacote, task):
        
        fluxo = vinerOnline.controle_fluxo(pacote)            
        
        if fluxo == vinerOnline.ALLOWED:
        
            acao = int(pacote.get_acao())
            
            if self.acoes_publicas.has_key(acao):
                self.acoes_publicas.get(acao).execute(pacote)                
            else: 
                
                addr_key    = pacote.get_endereco().get_key_addr()
                obj_usuario = vinerOnline.busca_usuario_on_por_addr(addr_key)
                
                if obj_usuario:
                    if self.acoes_privadas.has_key(acao):                    
                        self.acoes_privadas.get(acao).execute(obj_usuario, pacote)                                                                                                    
                    else:                                    
                        print "Nao processo"
                    
                else:
                    #COMUNICA AO USUARIO QUE ELE NAO ESTA CONECTADO NO SERVIDOR
                    vinerOnline.envia_pacote(pacote.get_endereco(), 1, ACAO_CLIENT_desconectar)
                    
        elif fluxo == vinerOnline.DENIED:
                        
            endereco = pacote.get_endereco().get_key_addr()            
            vinerOnline.remove_usuario(endereco)

        elif fluxo == vinerOnline.PASSED:
            print "PASSED %s" % pacote.get_sequencia()
            
        return task.done