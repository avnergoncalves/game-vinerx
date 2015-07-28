'''
Created on 09/02/2012

@author: viner
'''
from Viner.Helpers.tools import get_path_modelo

class Mapa(object):
    '''    
    '''

    def __init__(self):
        '''
        '''        
        pandafile = get_path_modelo("world")
        
        self.modelo = loader.loadModel(pandafile)
        self.modelo.reparentTo(render)
        self.modelo.setPos(0,0,0)        