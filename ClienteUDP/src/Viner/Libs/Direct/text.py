'''
Created on 01/02/2012

@author: avner.goncalves
'''
from panda3d.core import TextNode

class Text(object):
    
    def __init__(self, parent   = None,
                       nameNode = '',
                       text     = None,
                       align    = 'left',
                       wordwrap = 0,
                       scale    = .05,
                       pos      = (0, 0, 0),
                       cor      = (1, 1, 1, 1)):            
        
        if align == 'center':
            align = TextNode.ACenter
        elif align == 'left':
            align = TextNode.ALeft
        elif align == 'rigth':
            align = TextNode.ARight
        else :
            align = TextNode.ALeft
        
        self.textNode = TextNode(nameNode)
        self.textNode.setTextColor(cor)            
        self.textNode.setAlign(align)
        self.textNode.setText(text)        
                
        self.textNode.setWordwrap(wordwrap)
        
        self.textNodePath = parent.attachNewNode(self.textNode)        
        self.textNodePath.setScale(scale)
        
        height = (scale*self.textNode.getNumRows())
        self.textNodePath.setPos((pos[0], pos[1], pos[2]+height))
            
    def remove(self):
        self.textNodePath.remove()
        
    def billboardEffect(self):
        self.textNodePath.setBillboardAxis()
        self.textNodePath.setBillboardPointWorld()
        self.textNodePath.setBillboardPointEye()
    
    def getScale(self):
        return self.textNodePath.getScale()[0]
    
    def setPos(self, pos):
        self.textNodePath.setPos(pos)                        