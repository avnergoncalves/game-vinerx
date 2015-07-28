'''
Created on 10/02/2012

@author: avner.goncalves
'''

from direct.gui.DirectGui import DirectFrame, DirectWaitBar

class ProgressBar(object):
    '''        
    '''
    def __init__(self):
        '''        
        '''
        self.__wait_bar = DirectWaitBar( text = "Carregando...",
                                         value = 0,
                                         pos = (0, 0, -.95),
                                         text_scale = 0.05,
                                         text_pos = (0, 0.025),
                                         frameSize = (-1.3, 1.3, 0, 0.08) )
        
        self.hide()
        
    def finish(self):
        self.__wait_bar['barColor'] = (0, 1, 0, 1)
        self.__wait_bar.setBarColor()
        self.__wait_bar.finish()
        self.hide()
    
    def hide(self):
        self.__wait_bar.hide()
        
    def show(self):
        self.__wait_bar.show()
        
    def update(self, value):
        
        if value < 25:
            self.__wait_bar['barColor'] = (1, 0, 0, 1)
        elif value > 25 and value < 75:
            self.__wait_bar['barColor'] = (1, 1, 0, 1)
        elif value > 75:
            self.__wait_bar['barColor'] = (0, 1, 0, 1)
            
            
        self.__wait_bar.setBarColor()
        
        self.__wait_bar.update(value)
        
        