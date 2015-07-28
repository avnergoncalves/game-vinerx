'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao

class ConfirmarPacote(object):
    
    def __init__(self):        
        pass    
    
    def confirmar(self, pacote):
        if not vinerOnline.clear_pacotes_confirmar(pacote):
            print 'Nao existe addr para confirmar o pacote'
        
class AcaoConfirmarPacote(Acao):
    
    def __init__(self, confirmar_pacote):
        self.confirmar_pacote = confirmar_pacote
        
    def execute(self, obj, pacote):                        
        self.confirmar_pacote.confirmar(pacote)