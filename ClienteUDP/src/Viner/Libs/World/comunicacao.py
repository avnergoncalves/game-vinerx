'''
Created on 19/04/2011

@author: avner.goncalves
'''

from vconstantes import TECLA_esquerda, TECLA_direita, TECLA_frente, TECLA_traz,\
        EVENT_down, EVENT_up, EVENT_nenhum
    
from Viner.Helpers.tools import get_acao_por_tecla


class Comunicacao(object):
    '''
    UsuarioPrincipal
    '''
    
    def __init__(self):
        '''
        '''
        self.__estaMovendo = False
        self.__estaRodando = False
        
        taskMgr.add(self.__task_comunicacao, 'Task Comunicacao', sort=2)
                
    def __task_inf(self, tecla, task):
        vinerOnline.envia_pacote_server(1, get_acao_por_tecla(tecla), [tecla, EVENT_nenhum])
        
        return task.again
    
    def __task_comunicacao(self, task):
        
        if vinerWorld.usuario.keyMap[TECLA_esquerda] == EVENT_down and vinerWorld.usuario.keyMap[TECLA_direita] == EVENT_up:                                
            if not self.__estaRodando:                
                taskMgr.doMethodLater(2,self.__task_inf,"InformaRotacao", extraArgs = [TECLA_esquerda],appendTask = True)
                #seta que esta rodando
                self.__estaRodando = True
            
        elif vinerWorld.usuario.keyMap[TECLA_direita] == EVENT_down and vinerWorld.usuario.keyMap[TECLA_esquerda] == EVENT_up:                        
            if not self.__estaRodando:                
                taskMgr.doMethodLater(2,self.__task_inf,"InformaRotacao", extraArgs = [TECLA_direita],appendTask = True)
                #seta que esta rodando
                self.__estaRodando = True                
            
        elif self.__estaRodando:
            #remove tareda
            taskMgr.remove("InformaRotacao")
            #seta que nao esta rodando
            self.__estaRodando = False
                                
            
        if vinerWorld.usuario.keyMap[TECLA_frente] == EVENT_down and vinerWorld.usuario.keyMap[TECLA_traz] == EVENT_up:                        
            if not self.__estaMovendo:                
                taskMgr.doMethodLater(2,self.__task_inf,"InformaMovimento", extraArgs = [TECLA_frente],appendTask = True)
                #seta que esta movimentando                
                self.__estaMovendo = True
                
        elif vinerWorld.usuario.keyMap[TECLA_traz] == EVENT_down and vinerWorld.usuario.keyMap[TECLA_frente] == EVENT_up:
            if not self.__estaMovendo:                
                taskMgr.doMethodLater(2,self.__task_inf,"InformaMovimento", extraArgs = [TECLA_traz],appendTask = True)
                #seta que esta movimentando
                self.__estaMovendo = True
                
        elif self.__estaMovendo:
            #remove tareda
            taskMgr.remove("InformaMovimento")
            #seta que nao esta movimentando
            self.__estaMovendo = False
            
        return task.cont