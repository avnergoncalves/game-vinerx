'''
Created on 06/05/2011

@author: avner.goncalves
'''

class RecebeProcessaComandos(object):
    '''
    ListenComandos
    '''

    def __init__(self):
        '''
        Constructor
        '''        
        self.__handler = None
    
    def setHandler(self, handler):
        '''
        Seta o manipulador de comandos
        '''
        self.__handler = handler
    
    def listen(self):
        '''
        Atende os comandos no prompt
        '''
        a = raw_input('>> ')
        self.__handler.execute_comando(a)            