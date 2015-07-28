'''
Created on 23/01/2012

@author: avner.goncalves
'''

class vUsuario(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.TIME_PRIMEIRO_PCK_RECV = -1
        self.QTD_PCK_RECV_POR_SEG   = 0            
                
        self.sq_ultimo_pacote_enviado  = 0
        self.sq_ultimo_pacote_recebido = 0
        self.tm_ultimo_pacote_enviado  = 0
        self.tm_ultimo_pacote_recebido = 0        