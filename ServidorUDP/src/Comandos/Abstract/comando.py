'''
Created on 29/04/2011

@author: avner.goncalves
'''

from abc import abstractmethod

class Comando(object):
    
    @abstractmethod
    def execute(self, *args):
        pass