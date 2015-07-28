'''
Created on 08/02/2012

@author: viner
'''

from Viner.Libs.Direct.text_scrolled_frame import TextScrolledFrame
from Viner.Libs.Direct.frame_autenticacao import FrameAutenticacao
from Viner.Libs.Direct.progress_bar import ProgressBar
from Viner.Libs.Direct.entry_button_frame import EntyButtonFrame

class VinerDirect(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.FrameMsgGeral     = TextScrolledFrame(parent=base.a2dBottomLeft)
        self.EnviarMsgGeral    = EntyButtonFrame(parent=base.a2dBottomLeft)
        self.FrameAutenticacao = FrameAutenticacao()
        self.ProgressBar       = ProgressBar()        
        