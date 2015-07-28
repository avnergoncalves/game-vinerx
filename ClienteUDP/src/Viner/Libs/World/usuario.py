'''
Created on 19/04/2011

@author: avner.goncalves
'''
from direct.actor.Actor import Actor
from panda3d.core import CollisionNode,CollisionTraverser
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import BitMask32

from vconstantes import TECLA_esquerda, TECLA_direita, TECLA_frente, TECLA_traz,\
    EVENT_down, EVENT_up

from Viner.Helpers.tools import get_path_modelo, get_path_animacao
from Viner.Libs.Direct.text import Text

from vConfigs.vconfig import SCALE_MODELOS

from Configs.cores import COR_VERDE

class Usuario(object):
    '''
    Usuario
    '''    
    def __init__(self, dadosUsuario, principal = False):
        self.key              = dadosUsuario['key']
        self.nick             = dadosUsuario['nick']
        self.vida_real        = float(dadosUsuario['vida_real'])
        self.vida_total       = float(dadosUsuario['vida_total'])
        self.mana_real        = float(dadosUsuario['mana_real'])
        self.mana_total       = float(dadosUsuario['mana_total'])        
        self.forca            = float(dadosUsuario['forca'])
        self.velocidade       = float(dadosUsuario['velocidade'])
        self.velocidade_atack = float(dadosUsuario['velocidade_atack'])
                            
        self.estaMovendo      = False
        self.estaRodando      = False        
        
        self.__task_name      = "Task Usuario - "+self.key
                    
        self.keyMap           = {TECLA_esquerda:EVENT_up, TECLA_direita:EVENT_up, TECLA_frente:EVENT_up, TECLA_traz:EVENT_up}
                
        pandaFileModelo       = get_path_modelo("ralph")
        pandaFileAnimacaoRun  = get_path_animacao("ralph-run")
        pandaFileAnimacaoWalk = get_path_animacao("ralph-walk")

        self.modelo = Actor(pandaFileModelo, {"run":pandaFileAnimacaoRun,"walk": pandaFileAnimacaoWalk})        
        self.modelo.reparentTo(render)
        self.modelo.setScale(SCALE_MODELOS)        
        
        self.set_pos((float(dadosUsuario['x']), float(dadosUsuario['y']), float(dadosUsuario['z'])))                
        self.set_h(float(dadosUsuario['h']))
                
        if not principal:
            self.text = Text( parent   = self.modelo,
                          pos      = (0,0,5.5),
                          scale    = .5,
                          align    = 'center',
                          cor      = COR_VERDE,
                          text     = self.nick)
        
            self.text.billboardEffect()
        
        self.__setup_collision()
        
        taskMgr.add(self.__task_movimentacao, self.__task_name, sort=1)
    
    def get_x(self):
        return self.modelo.getX()
    
    def get_y(self):
        return self.modelo.getY()
    
    def get_z(self):
        return self.modelo.getZ()
    
    def get_h(self):        
        return self.modelo.getH()
    
    def get_pos(self):
        return self.modelo.getPos()
    
    def set_x(self, x):        
        self.modelo.setX(x)
        
    def set_y(self, y):            
        self.modelo.setY(y)
        
    def set_z(self, z):            
        self.modelo.setZ(z)
        
    def set_h(self, h):        
        self.modelo.setH(h)
        
    def set_pos(self, pos):        
        self.modelo.setPos(pos)        
    
    def delete(self):        
        taskMgr.remove(self.__task_name)
        
        self.modelo.delete()
    
    def __setup_collision(self):
        #Colisao
        self.cTrav = CollisionTraverser('usuarioTraverser')
                
        self.ralphGroundRay = CollisionRay()
        self.ralphGroundRay.setOrigin(0,0,5)
        self.ralphGroundRay.setDirection(0,0,-1)
        self.ralphGroundCol = CollisionNode('ralphRay')
        self.ralphGroundCol.addSolid(self.ralphGroundRay)
        self.ralphGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.ralphGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.ralphGroundColNp = self.modelo.attachNewNode(self.ralphGroundCol)
        self.ralphGroundHandler = CollisionHandlerQueue()        
        
        self.cTrav.addCollider(self.ralphGroundColNp, self.ralphGroundHandler)
        
        #self.ralphGroundColNp.show()
        #self.cTrav.showCollisions(render)
        #Colisao
    
    def __task_movimentacao(self, task):
        dt       = globalClock.getDt() 
        startpos = self.modelo.getPos()            
        
        #movimentos usuario modelo
        if self.keyMap[TECLA_esquerda] == EVENT_down and self.keyMap[TECLA_direita] == EVENT_up:            
            self.modelo.setH(self.modelo, ((self.velocidade*5) * dt))                                        

            if not self.estaRodando:
                self.estaRodando = True
            
        elif self.keyMap[TECLA_direita] == EVENT_down and self.keyMap[TECLA_esquerda] == EVENT_up:
            self.modelo.setH(self.modelo, ((self.velocidade*5) * dt)*-1)
            
            if not self.estaRodando:
                self.estaRodando = True
                
        elif self.estaRodando:
            self.estaRodando = False                    
        
        if self.keyMap[TECLA_frente] == EVENT_down and self.keyMap[TECLA_traz] == EVENT_up:            
            self.modelo.setY(self.modelo, ((self.velocidade*2) * dt)*-1)
            
            if self.estaMovendo is False:
                self.modelo.loop("run")
                self.estaMovendo = True
                
        elif self.keyMap[TECLA_traz] == EVENT_down and self.keyMap[TECLA_frente] == EVENT_up:            
            self.modelo.setY(self.modelo, (self.velocidade * dt))
            
            if self.estaMovendo is False:
                self.modelo.loop("walk")
                self.estaMovendo = True
                
        elif self.estaMovendo:
            self.modelo.stop()
            self.modelo.pose("walk",5)
            self.estaMovendo = False
        #movimentos usuario modelo        
        
        if self.estaMovendo:
            
            self.cTrav.traverse(render)
                                        
            if self.ralphGroundHandler.getNumEntries() == 1:            
                entry = self.ralphGroundHandler.getEntry(0)
                if entry.getIntoNode().getName() == "terrain":
                    self.modelo.setZ(entry.getSurfacePoint(render).getZ())
            else:                
                self.modelo.setPos(startpos)
        
        return task.cont        