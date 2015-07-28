'''
Created on 09/02/2012

@author: viner
'''
from panda3d.core import CollisionTraverser

from Viner.Libs.World.mapa import Mapa

class VinerWorld(object):
    '''
    '''

    def __init__(self):
        '''
        '''        
        #carrega traverser de colisao
        base.cTrav = CollisionTraverser()        
        
        self.mapa = Mapa()        