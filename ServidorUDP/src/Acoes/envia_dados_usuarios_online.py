'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao
from vconstantes import ACAO_CLIENT_conectar

class EnviaDadosUsuariosOnline(object):
    '''
    Acao resposavel por enviar todos os usuarios que estao online
    para atualizar a lista do novo usuario conectado    
    '''
    
    def __init__(self):        
        pass
    
    def enviar(self, obj_usuario):                
        obj_usuario_dic = vinerOnline.get_obj_usuario_on_dic()
        
        for i in obj_usuario_dic:
            if obj_usuario.key != i:                
                dadosUsuario =  obj_usuario_dic[i].get_dados()
                
                msg = ['1',]
                msg.extend(dadosUsuario)                                    
                vinerOnline.envia_pacote(obj_usuario.addr, 0, ACAO_CLIENT_conectar, msg)
                
        obj_usuario.habilitado = True
        
class AcaoEnviaDadosUsuariosOnline(Acao):
    
    def __init__(self, envia_dados_usuarios_online):
        self.envia_dados_usuarios_online = envia_dados_usuarios_online
        
    def execute(self, obj_usuario, pacote):                
        self.envia_dados_usuarios_online.enviar(obj_usuario)