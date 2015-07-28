'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao

class VerificaStatus(object):
    
    def __init__(self):        
        pass
    
    def verificar(self, obj_usuario):
        pass
        
class AcaoVerificaStatus(Acao):
    
    def __init__(self, verifica_status):
        self.verifica_status = verifica_status
        
    def execute(self, obj_usuario, pacote):
        print ' %s Verificou o Status' % (obj_usuario.nick)
                
        self.verifica_status.verificar(obj_usuario)