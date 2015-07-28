'''
Created on 01/02/2012

@author: avner.goncalves
'''
from direct.gui.DirectGui import DirectScrolledFrame
from text import Text
from Configs.cores import COR_OPACITY_03_PRETO

class TextScrolledFrame(object):    

    def __init__(self, parent    = None
                     , scale     = .05
                     , limitText = 1                     
                     , frameSize = (0, 1.3, .2, .697)
                     , pos       = (0, 0, .1)):
        
        self.__scale      = scale
        self.__frameSize  = frameSize
        self.__canvasSize = (frameSize[0], frameSize[2]-.01, frameSize[2], frameSize[3])        
        self.__limitText  = limitText
        self.__countLine  = []
                    
        self.dsf = DirectScrolledFrame( parent             = parent,
                                        canvasSize         = self.__canvasSize, 
                                        frameSize          = self.__frameSize,
                                        pos                = pos,
                                        frameColor         = COR_OPACITY_03_PRETO,                                    
                                        autoHideScrollBars = 1, 
                                        scrollBarWidth     = 0.05,
                                        borderWidth        = (0, 0),
                                                                            
                                        verticalScroll_value                   = 1,                                                                            
                                        
                                        verticalScroll_decButton_frameColor    = (1,1,1,0.3),                                        
                                        verticalScroll_decButton_rolloverSound = None,
                                        verticalScroll_decButton_clickSound    = None,
                                         
                                        verticalScroll_incButton_frameColor    = (1,1,1,0.3),                                        
                                        verticalScroll_incButton_rolloverSound = None,
                                        verticalScroll_incButton_clickSound    = None,
                                         
                                        verticalScroll_thumb_frameColor        = (1,1,1,0.3),                                        
                                        verticalScroll_thumb_rolloverSound     = None,
                                        verticalScroll_thumb_clickSound        = None )
                            
        self.__textoHeight   = scale        
        self.__canvasHeight  = self.dsf.getHeight()
        self.__canvas        = self.dsf.getCanvas()
    
    def __command_clear_msg(self):
        self.etyMsg.set("")
    
    def __reposicionaTexto(self, obj_text):
        height = obj_text.getScale()*obj_text.textNode.getNumRows()
        
        for text in self.__countLine:
            lastPos = text.textNodePath.getPos()
            text.setPos((lastPos[0], 0, lastPos[2]+height))    
    
    def __resizeCanvasSize(self, text):        
                    
        self.__textoHeight += text.getScale()*text.textNode.getNumRows()            
        
        
        if self.__textoHeight > self.__canvasHeight:            
            self.__canvasHeight += self.__textoHeight - self.__canvasHeight
        
        self.dsf['canvasSize'] = ( self.dsf['canvasSize'][0],
                                   self.dsf['canvasSize'][1], 
                                   self.dsf['canvasSize'][2], 
                                   self.dsf['canvasSize'][2] + self.__canvasHeight )        
        self.dsf.setCanvasSize()
                                    
    def show(self, texto, cor = (1, 1, 1, 1)):
        
        dfs_pos = self.dsf.getPos()
                             
        pos  = (dfs_pos[0]+.01, 0, dfs_pos[1]+0.16)            
                        
        text = Text( parent   = self.__canvas,
                     scale    = self.__scale,
                     text     = texto,
                     wordwrap = 25,               
                     pos      = pos,
                     cor      = cor )            
        
        numText = len(self.__countLine)
        if numText > 0:            
            self.__reposicionaTexto(text)            
                    
        self.__countLine.append(text)
        
        if numText > self.__limitText:            
            self.__countLine[0].remove()
            self.__countLine.pop(0)
        else:
            self.__resizeCanvasSize(text)
            
        self.dsf['verticalScroll_value'] = 1        
