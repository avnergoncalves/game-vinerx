'''
Created on 19/04/2011

@author: avner.goncalves
'''
import time

from vconstantes import TECLA_esquerda, TECLA_direita, TECLA_frente, TECLA_traz,\
    EVENT_down, EVENT_up, ACAO_CLIENT_rodar, ACAO_CLIENT_mover

from direct.actor.Actor import Actor

from panda3d.core import CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import BitMask32

from vConfigs.vconfig import SCALE_MODELOS

from Viner.Helpers.tools import get_path_modelo

class Usuario(object):
    '''
    Usuario
    '''
        
    def __init__(self):                
        self.habilitado      = False
        
        self.estaMovendo     = False
        self.estaRodando     = False
        self.timeIniMover    = 0
        self.timeIniRodar    = 0
        self.keyMap          = {TECLA_esquerda:EVENT_up, TECLA_direita:EVENT_up, TECLA_frente:EVENT_up, TECLA_traz:EVENT_up}            
                        
        self.login            = None
        self.senha            = None
        self.nick             = None
        
        self.vida_real        = None
        self.vida_total       = None
        self.mana_real        = None
        self.mana_total       = None        
        self.forca            = None
        self.velocidade       = None
        self.velocidade_atack = None            
        
        self.key              = None
        self.addr             = None
        self.login            = None            
        
        pandaFileModelo = get_path_modelo("ralph")
        
        self.__modelo = Actor(pandaFileModelo)
        self.__modelo.reparentTo(render)
        self.__modelo.setScale(SCALE_MODELOS)
        
        modeloStartPos = vinerWorld.mapa.modelo.find("**/start_point").getPos()
        self.set_pos(modeloStartPos)
        
        self.__setup_collision()
    
    def get_x(self):
        return self.__modelo.getX()
    
    def get_y(self):
        return self.__modelo.getY()
    
    def get_z(self):
        return self.__modelo.getZ()    
    
    def get_h(self):
        return self.__modelo.getH()
    
    def get_pos(self):
        return self.__modelo.getPos()
            
    def set_x(self, x):
        self.__modelo.setX(x)
        
    def set_y(self, y):            
        self.__modelo.setY(y)
        
    def set_z(self, z):            
        self.__modelo.setZ(z)

    def set_h(self, h):        
        self.__modelo.setH(h)
        
    def set_pos(self, pos):
        self.__modelo.setPos(pos)    
    
    def get_dados(self):
        
        return [self.key,
                self.nick,
                self.vida_real,
                self.vida_total,
                self.mana_real,
                self.mana_total,
                self.forca,
                self.velocidade,
                self.velocidade_atack,
                self.get_x(),
                self.get_y(),
                self.get_z(),
                self.get_h(),]
    
    def stop_task_movimentacao(self):        
        taskMgr.remove(self.key)
        
    def inicia_task_movimentacao(self):
        if self.key != "":            
            taskMgr.add(self.__task_movimentacao, self.key, sort=1)
    
    def __setup_collision(self):
        #Colisao        
        self.ralphGroundRay = CollisionRay()
        self.ralphGroundRay.setOrigin(0,0,5)
        self.ralphGroundRay.setDirection(0,0,-1)
        self.ralphGroundCol = CollisionNode('ralphRay')
        self.ralphGroundCol.addSolid(self.ralphGroundRay)
        self.ralphGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.ralphGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.ralphGroundColNp = self.__modelo.attachNewNode(self.ralphGroundCol)
        self.ralphGroundHandler = CollisionHandlerQueue()
                
        base.cTrav.addCollider(self.ralphGroundColNp, self.ralphGroundHandler)
        #Colisao
                  
    def __task_movimentacao(self, task):
        dt       = globalClock.getDt()
        startpos = self.__modelo.getPos()            
        
        #rodar usuario
        if self.keyMap[TECLA_esquerda] == EVENT_down and self.keyMap[TECLA_direita] == EVENT_up:

            if time.time() < self.timeIniRodar+4:
                self.estaRodando = True
                            
                self.__modelo.setH(self.__modelo, ((self.velocidade*5) * dt))                
            else:
                h = self.get_h()            
                vinerOnline.envia_pacote_todos(1,ACAO_CLIENT_rodar,[self.key, TECLA_esquerda, EVENT_up, h])
                
                self.estaRodando = False                
                self.keyMap[TECLA_esquerda] = EVENT_up
                                                                                
        elif self.keyMap[TECLA_direita] == EVENT_down and self.keyMap[TECLA_esquerda] == EVENT_up:                    
                        
            if time.time() < self.timeIniRodar+4:
                self.estaRodando = True
                            
                self.__modelo.setH(self.__modelo, ((self.velocidade*5) * dt)*-1)
            else:
                h = self.get_h()            
                vinerOnline.envia_pacote_todos(1,ACAO_CLIENT_rodar,[self.key, TECLA_direita, EVENT_up, h])
                
                self.estaRodando = False                
                self.keyMap[TECLA_direita] = EVENT_up                            
        elif self.estaRodando:
            self.estaRodando = False
        #rodar usuario
        
        #mover usuario  
        if self.keyMap[TECLA_frente] == EVENT_down and self.keyMap[TECLA_traz] == EVENT_up:
                                
            if time.time() < self.timeIniMover+4:
                self.estaMovendo = True
                            
                self.__modelo.setY(self.__modelo, ((self.velocidade*2) * dt)*-1)
            else:
                x = self.get_x()
                y = self.get_y()
                z = self.get_z()                                
                vinerOnline.envia_pacote_todos(1,ACAO_CLIENT_mover,[self.key,TECLA_frente,EVENT_up,x,y,z])
                
                self.estaMovendo = False                
                self.keyMap[TECLA_frente] = EVENT_up
                                                        
        elif self.keyMap[TECLA_traz] == EVENT_down and self.keyMap[TECLA_frente] == EVENT_up:            
                                
            if time.time() < self.timeIniMover+4:
                self.estaMovendo = True
                            
                self.__modelo.setY(self.__modelo, (self.velocidade * dt))
            else:
                x = self.get_x()
                y = self.get_y()
                z = self.get_z()                                
                vinerOnline.envia_pacote_todos(1,ACAO_CLIENT_mover,[self.key,TECLA_traz,EVENT_up,x,y,z])
                
                self.estaMovendo = False                
                self.keyMap[TECLA_traz] = EVENT_up
                                                        
        elif self.estaMovendo:            
            self.estaMovendo = False
        #mover usuario
        
        #se esta moventdo trata colisao
        if self.estaMovendo:

            base.cTrav.traverse(render)
            
            if self.ralphGroundHandler.getNumEntries() == 1:            
                entry = self.ralphGroundHandler.getEntry(0)
                if entry.getIntoNode().getName() == "terrain":
                    self.__modelo.setZ(entry.getSurfacePoint(render).getZ())
            else:                
                self.__modelo.setPos(startpos)
        #se esta moventdo trata colisao
    
        return task.cont            