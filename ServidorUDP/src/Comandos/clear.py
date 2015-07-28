'''
Created on 29/04/2011

@author: avner.goncalves
'''

import os
from Abstract.comando import Comando


class Clear(object):
    
    def __init__(self):        
        pass
    
    def limpar_tela(self):        
        os.system("cls")
        
class AcaoClear(Comando):
    
    def __init__(self, clear):
        self.clear = clear
        
    def execute(self, *args):                
        self.clear.limpar_tela()