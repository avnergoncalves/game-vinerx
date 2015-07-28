'''
Created on 29/04/2011

@author: avner.goncalves
'''
import time

from Abstract.acao import Acao

from vconstantes import ACAO_CLIENT_mover, TECLA_frente,\
    TECLA_traz, EVENT_down, EVENT_up, EVENT_nenhum

class Mover(object):
    
    def __init__(self):        
        pass
    
    def enviar_movimento(self, obj_usuario, tecla, event):
        
        obj_usuario.timeIniMover = time.time()
        
        if event != EVENT_nenhum:
            obj_usuario.keyMap[tecla] = event
            
            if (obj_usuario.keyMap[TECLA_frente] == EVENT_down and obj_usuario.keyMap[TECLA_traz] == EVENT_down) \
            or (obj_usuario.keyMap[TECLA_frente] == EVENT_up and obj_usuario.keyMap[TECLA_traz] == EVENT_up):
                x = obj_usuario.get_x()
                y = obj_usuario.get_y()
                z = obj_usuario.get_z()
                                
                vinerOnline.envia_pacote_todos(1,ACAO_CLIENT_mover,[obj_usuario.key,tecla,event,x,y,z])
            else:
                vinerOnline.envia_pacote_todos(1,ACAO_CLIENT_mover,[obj_usuario.key,tecla,event],[obj_usuario.key])                

class AcaoMover(Acao):
    
    def __init__(self, mover):
        self.mover = mover
        
    def execute(self, obj_usuario, pacote):
        
        tecla = pacote.get_arg(0)
        event = pacote.get_arg(1)
        
        self.mover.enviar_movimento(obj_usuario, tecla, event)