'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao

class Desconectar(object):
    
    def __init__(self):        
        pass
    
    def remover_usuario(self, addr):
        vinerOnline.remove_usuario(addr)
        
class AcaoDesconectar(Acao):
    
    def __init__(self, drop_usuario):
        self.drop_usuario = drop_usuario
        
    def execute(self, obj_usuario, pacote):                            
        self.drop_usuario.remover_usuario(obj_usuario.addr)