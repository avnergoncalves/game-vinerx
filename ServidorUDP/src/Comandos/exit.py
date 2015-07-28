'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.comando import Comando

class Exit(object):
    
    def __init__(self):        
        pass
    
    def fechar(self):
        obj_trf_exc_list = vinerOnline.get_tarefa_exc_list()              
        
        for trf in obj_trf_exc_list:
            trf.stop()
                    
        vinerOnline.shutdown()
        print '--Servidor Off--'
        
class AcaoExit(Comando):
    
    def __init__(self, exite):
        self.exit = exite
        
    def execute(self, *args):                
        self.exit.fechar()