'''
Created on 29/04/2011

@author: avner.goncalves
'''
import time

from Abstract.acao import Acao

from vconstantes import ACAO_CLIENT_rodar, TECLA_direita,\
    TECLA_esquerda, EVENT_nenhum, EVENT_up, EVENT_down


class Rodar(object):
    
    def __init__(self):        
        pass
    
    def enviar_rotacao(self, obj_usuario, tecla, event):            
        
        obj_usuario.timeIniRodar = time.time()
        
        if event != EVENT_nenhum:                
            obj_usuario.keyMap[tecla] = event
            
            if (obj_usuario.keyMap[TECLA_direita] == EVENT_down and obj_usuario.keyMap[TECLA_esquerda] == EVENT_down) \
            or (obj_usuario.keyMap[TECLA_direita] == EVENT_up and obj_usuario.keyMap[TECLA_esquerda] == EVENT_up):
                h = obj_usuario.get_h()
            
                vinerOnline.envia_pacote_todos(1,ACAO_CLIENT_rodar,[obj_usuario.key, tecla, event, h])
            else:
                vinerOnline.envia_pacote_todos(1,ACAO_CLIENT_rodar,[obj_usuario.key, tecla, event],[obj_usuario.key])                                            
        
class AcaoRodar(Acao):
    
    def __init__(self, rodar):
        self.rodar = rodar
        
    def execute(self, obj_usuario, pacote):
                
        tecla = pacote.get_arg(0)
        event = pacote.get_arg(1)
                                
        self.rodar.enviar_rotacao(obj_usuario, tecla, event)