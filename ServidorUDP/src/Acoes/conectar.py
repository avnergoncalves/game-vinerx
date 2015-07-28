'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao
                        
from vconstantes import ACAO_CLIENT_conectar, RESPOSTA_USU_PRINCIPAL_CONECTADO,\
                        RESPOSTA_USU_NOVO_CONECTADO, RESPOSTA_DADOS_INVALIDO

class Conectar(object):
    
    def __init__(self):        
        pass
    
    def __adiciona_usuario(self, endereco, login):                                                        
                
        obj_usuario = vinerOnline.registra_usuario(endereco, login)                                
        
        dadosUsuario =  obj_usuario.get_dados()
        
        #Envia para o usuario sua chave
        msg = [RESPOSTA_USU_PRINCIPAL_CONECTADO]        
        msg.extend(dadosUsuario)        
        vinerOnline.envia_pacote(endereco, 0, ACAO_CLIENT_conectar, msg)
                
        #Envia para todos os outros usuarios a chave do novo usuario exceto para o usuario novo
        msg = [RESPOSTA_USU_NOVO_CONECTADO]
        msg.extend(dadosUsuario)           
        vinerOnline.envia_pacote_todos(0, ACAO_CLIENT_conectar, msg, [obj_usuario.key])
        
    def __is_autenticado(self, login, senha):
        '''
        Carrega e Registra o usuario no Servidor.
        '''
        retorno = False
        
        obj_usuarios_off = vinerOnline.get_obj_usuario_off_dic()
             
        if obj_usuarios_off.has_key(login):            
            obj_usuario = obj_usuarios_off.get(login)
            
            if obj_usuario.senha == senha :            
                retorno = True          
                                            
        return retorno
    
    def conecta_usuario(self, pacote):
                    
        login    = pacote.get_arg(0)
        senha    = pacote.get_arg(1)
        endereco = pacote.get_endereco()
        
        if self.__is_autenticado(login, senha):                                
            self.__adiciona_usuario(endereco, login)
        else:
            vinerOnline.envia_pacote(endereco, 1, ACAO_CLIENT_conectar, [RESPOSTA_DADOS_INVALIDO])
        
class AcaoConectar(Acao):
    
    def __init__(self, conectar_usuario):
        self.conectar_usuario = conectar_usuario
        
    def execute(self, pacote):                        
        self.conectar_usuario.conecta_usuario(pacote)