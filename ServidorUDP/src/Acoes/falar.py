'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao

from vconstantes import ACAO_CLIENT_falar

class Falar(object):
    
    def enviar(self, mensagem, obj_usuario_remetente):
        
        if mensagem[0] == '/':
            
            posEspaco =  mensagem.find(" ")
            
            if posEspaco == -1: posEspaco = len(mensagem)                    
            
            login = mensagem[1:posEspaco]
                        
            obj_usuario = vinerOnline.busca_usuario_on_por_login(login)
            
            if obj_usuario:
                mensagem = mensagem[posEspaco:]
                vinerOnline.envia_pacote(obj_usuario_remetente.addr, 0, ACAO_CLIENT_falar,  [mensagem, obj_usuario_remetente.key, 1])
                vinerOnline.envia_pacote(obj_usuario.addr, 0, ACAO_CLIENT_falar,  [mensagem, obj_usuario_remetente.key, 2])                
                
            else:
                obj_usuario = vinerOnline.busca_usuario_off_por_login(login)
                if obj_usuario:
                    #enviar msg de usuario offine
                    pass
                else:
                    #enviar msg de usuario nao existe
                    pass            
                                    
                                    
        else:
            vinerOnline.envia_pacote_todos(0, ACAO_CLIENT_falar, [mensagem, obj_usuario_remetente.key, 1])
            
    
class AcaoFalar(Acao):
    
    def __init__(self, falar):
        self.falar = falar
        
    def execute(self, obj_usuario, pacote):
        mensagem    = pacote.get_arg(0)        

        self.falar.enviar(mensagem, obj_usuario)