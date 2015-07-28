'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao

class Rodar(object):
    
    def __init__(self):        
        pass
    
    def enviar_rotacao(self, key_usuario, tecla, event, h):
        obj_usuario = vinerOnline.busca_usuario_por_key(key_usuario)
        
        if key_usuario != vinerWorld.usuario.key:
            obj_usuario.keyMap[tecla] = event                
        
        if h != "":
            h = float(h)
            
            if int(obj_usuario.modelo.getH()) != int(h):
                obj_usuario.set_h(float(h))
        
class AcaoRodar(Acao):
    
    def __init__(self, rodar):
        self.rodar = rodar
        
    def execute(self, pacote):
                
        key_usuario = pacote.get_arg(0)
        tecla       = pacote.get_arg(1)
        event       = pacote.get_arg(2)
        h           = pacote.get_arg(3)
        
        self.rodar.enviar_rotacao(key_usuario, tecla, event, h)