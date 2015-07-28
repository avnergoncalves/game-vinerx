'''
Created on 03/09/2012

@author: viner
'''

from panda3d.core import CollisionNode,CollisionSegment
from panda3d.core import CollisionTraverser,CollisionHandlerQueue
from panda3d.core import BitMask32

from vconstantes import EVENT_up

from Viner.Helpers.tools import hidden_mouse


class Camera(object):
    '''
        Controle da camera
    '''

    def __init__(self):
                        
        self.keyMap          = {"mouse1":EVENT_up,"wheel-in":EVENT_up,"wheel-out":EVENT_up}            
        
        self.__camSeg        = None
        self.__camColHandler = None
        self.__mousex        = 0
        self.__mousey        = 0
        self.__click         = False
                
        self.__camDistancia  = 200
        self.__camP          = 10
        self.__camRef        = 2.0
        
        self.ponto  = render.attachNewNode('ponto')
        self.ponto.reparentTo(vinerWorld.usuario.modelo)        
        self.ponto.setPos(0,0,self.__camRef)
        #self.ponto.show()
                
        base.camera.reparentTo(self.ponto)        
        base.camera.setY(base.camera, self.__camDistancia)
        
        self.__setup_collision()
        
        taskMgr.add(self.__task_movimentar_camera, "Task Camera", sort=3)
    
    def __setup_collision(self):
        
        self.cTrav = CollisionTraverser('cameraTraverser')
        
        self.__camSeg = CollisionSegment((0,0,self.__camRef),(0,0,0))
        
        cameraCol = CollisionNode('cameraSeg')
        cameraCol.addSolid(self.__camSeg)
        cameraCol.setFromCollideMask(BitMask32.bit(0))
        cameraCol.setIntoCollideMask(BitMask32.allOff()) 
               
        cameraColNp = self.ponto.attachNewNode(cameraCol)
                
        self.__camColHandler = CollisionHandlerQueue()
        
        self.cTrav.addCollider(cameraColNp, self.__camColHandler)
        
        #cameraColNp.show()
        #self.cTrav.showCollisions(render)
        
    def __task_movimentar_camera(self, task):
        
        if base.mouseWatcherNode.hasMouse():
            
            # Se rodar o botao do mouse, zoom-in ou zoom-out
            if self.keyMap["wheel-in"] != EVENT_up:                
                self.__camDistancia -= 0.1 * self.__camDistancia;
                if self.__camDistancia < 10:
                    self.__camDistancia = 10
                                            
                self.keyMap["wheel-in"] = EVENT_up
                
            elif self.keyMap["wheel-out"] != EVENT_up:
                self.__camDistancia += 0.1 * self.__camDistancia;
                if self.__camDistancia > 400:
                    self.__camDistancia = 400
                
                self.keyMap["wheel-out"] = EVENT_up
            # Se rodar o botao do mouse, zoom-in ou zoom-out
                                
            if self.keyMap["mouse1"] != EVENT_up:
                hidden_mouse(True)

                if not self.__click:
                    self.__click = True
                    self.__mousex = base.win.getPointer(0).getX()
                    self.__mousey = base.win.getPointer(0).getY()
                    
                mousex_atual = base.win.getPointer(0).getX()
                mousey_atual = base.win.getPointer(0).getY()

                deltaX = mousex_atual-self.__mousex
                deltaY = mousey_atual-self.__mousey

                #movimenta cam esquerda e direita
                self.ponto.setH(self.ponto, (0.5* deltaX))
                #movimenta cam esquerda direita

                #movimenta cam cima e baixo
                self.__camP += (0.5 * deltaY)

                if   (self.__camP < -60): self.__camP = -60
                elif (self.__camP >  80): self.__camP =  80
                #movimenta cam cima e baixo
                
                base.win.movePointer(0, self.__mousex, self.__mousey)
            else:
                hidden_mouse(False)
                self.__click = False
                
                if vinerWorld.usuario.estaMovendo:
                    #corrige cam automaticamente
                    ponto_h = int(self.ponto.getH())                    
                    if   (ponto_h > 0): self.ponto.setH(self.ponto, -1)
                    elif (ponto_h < 0): self.ponto.setH(self.ponto, +1)
                    #else:               self.ponto.setH(0)                                    
                    
                    comera_p = round(self.__camP,1)                    
                    if   (comera_p > 30.1): self.__camP -= 0.2
                    elif (comera_p < -0.1): self.__camP += 0.2                    
                    #corrige cam automaticamente                                        
        
        #atualiza posicao camera
        base.camera.setHpr(0,self.__camP,0)
        base.camera.setPos(0,0,0)
        base.camera.setY(base.camera, self.__camDistancia)
        base.camera.lookAt(self.ponto)
        
        self.__camSeg.setPointB(base.camera.getPos())
        #atualiza posicao camera
                
        #sistema de colisao
        self.cTrav.traverse(render)
        
        entries = []
        for i in range(self.__camColHandler.getNumEntries()):
            entry = self.__camColHandler.getEntry(i)
            entries.append(entry)
            
        entries.sort(lambda x,y: cmp(-y.getSurfacePoint(self.ponto).getY(),-x.getSurfacePoint(self.ponto).getY()))
        if (len(entries)>0):

            pColision = entries[0].getSurfacePoint(self.ponto)
            base.camera.setPos(pColision[0], pColision[1], pColision[2])
            
            if (entries[0].getIntoNode().getName() == "terrain"):
                base.camera.setZ(base.camera, 0.3)
        #sistema de colisao
        
        return task.cont