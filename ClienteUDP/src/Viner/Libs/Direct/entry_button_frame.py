'''
Created on 01/02/2012

@author: avner.goncalves
'''
from direct.gui.DirectGui import DirectFrame, DirectEntry, DirectButton

from vconstantes import ACAO_SERVER_falar

class EntyButtonFrame(object):

    def __init__(self, parent    = None
                     , scale     = .05
                     , limitText = 100                     
                     , frameSize = (0, 1.3, 0.11, .2)
                     , pos       = (0, 0, .1)):
        
        self.__show = True
        
        
        self.frmMsg = DirectFrame( parent     = parent,
                                   frameColor = (0,0,0,.5),
                                   frameSize  = frameSize, 
                                   pos        = pos,                                      
                                   enableEdit = 1 )
        
        self.etyMsg = DirectEntry( frameColor    = (1,1,1,.5),
                                   scale          = scale,
                                   width          = 22,
                                   numLines       = 1,
                                   pos            = (.02, 0, .14),
                                   cursorKeys     = 1,
                                   focus          = 1,
                                   command        = self.__command_enviar_msg,                                   
                                   focusInCommand = self.__command_clear_msg)
        
        
        self.btnMsgr = DirectButton( frameColor    = (0,0,0,1),
                                     text          = "Enviar",
                                     scale         = scale,
                                     pos           = (1.21, 0, .14),
                                     text_fg       = (1,1,1,1),                                                                                   
                                     rolloverSound = None,
                                     clickSound    = None,
                                     command       = self.__command_enviar_msg)
        
        
        self.etyMsg.reparentTo(self.frmMsg)
        self.btnMsgr.reparentTo(self.frmMsg)
        
        self.hide() 
    
    def hide(self):
        self.frmMsg.hide()
        self.__show = False
        
    def show(self):
        self.frmMsg.show()
        self.__show = True
        
        self.etyMsg.setFocus()
    
    def isShowing(self):
        return self.__show
     
    def __command_clear_msg(self):
        self.etyMsg.set("")
        
    def __command_enviar_msg(self, txt = None):
        
        msg = self.etyMsg.get()
        
        if msg != "":
            vinerOnline.envia_pacote_server(0, ACAO_SERVER_falar, [msg])
            self.__command_clear_msg()
            self.etyMsg.setFocus()        
        return False
        