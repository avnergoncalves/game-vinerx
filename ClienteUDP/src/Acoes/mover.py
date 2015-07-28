'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao

class Mover(object):
    
    def __init__(self):
        pass
    
    def mover_modelo(self, key_usuario, tecla, event, x,y,z):        
        obj_usuario = vinerOnline.busca_usuario_por_key(key_usuario)            
        
        if key_usuario != vinerWorld.usuario.key:
            obj_usuario.keyMap[tecla] = event
                  
        if x != "" and y != "" and z != "":
            x = float(x)
            y = float(y)
            z = float(z)
                        
            if int(obj_usuario.get_x()) != int(x) or int(obj_usuario.get_y()) != int(y) or int(obj_usuario.get_z()) != int(z):
                obj_usuario.set_x(x)
                obj_usuario.set_y(y)
                obj_usuario.set_z(z)                
        
                                
        
class AcaoMover(Acao):
    
    def __init__(self, mover):
        self.mover = mover
        
    def execute(self, pacote):
        
        key_usuario = pacote.get_arg(0)
        tecla       = pacote.get_arg(1)
        event       = pacote.get_arg(2)
        x           = pacote.get_arg(3)
        y           = pacote.get_arg(4)
        z           = pacote.get_arg(5)
        
        self.mover.mover_modelo(key_usuario, tecla, event, x,y,z)