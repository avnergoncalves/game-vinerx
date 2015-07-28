'''
Created on 10/02/2012

@author: viner
'''

import sys

from direct.showbase.DirectObject import DirectObject

from vconstantes import TECLA_esquerda, TECLA_direita, TECLA_frente, TECLA_traz,\
    EVENT_down, EVENT_up

from Viner.Helpers.tools import get_acao_por_tecla

class Evento(DirectObject):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''                
        
        self.accept("escape", sys.exit)
        
        self.accept("a", self.__setKeyUsuario, [TECLA_esquerda,EVENT_down])
        self.accept("d", self.__setKeyUsuario, [TECLA_direita,EVENT_down])
        self.accept("w", self.__setKeyUsuario, [TECLA_frente,EVENT_down])
        self.accept("s", self.__setKeyUsuario, [TECLA_traz,EVENT_down])
        
        self.accept("a-up", self.__setKeyUsuario, [TECLA_esquerda,EVENT_up])
        self.accept("d-up", self.__setKeyUsuario, [TECLA_direita,EVENT_up])
        self.accept("w-up", self.__setKeyUsuario, [TECLA_frente,EVENT_up])
        self.accept("s-up", self.__setKeyUsuario, [TECLA_traz, EVENT_up])
        
        self.accept("mouse1", self.__setKeyCamera, ["mouse1",EVENT_down])        
        self.accept("mouse1-up", self.__setKeyCamera, ["mouse1",EVENT_up])
        
        self.accept("wheel_up", self.__setKeyCamera, ["wheel-in", EVENT_down])
        self.accept("wheel_down", self.__setKeyCamera, ["wheel-out", EVENT_down])
        
        self.accept("enter", self.__setEventEnter)            
    
    def __setKeyUsuario(self, tecla, value):
        
        if vinerDirect.EnviarMsgGeral.isShowing():
            
            if vinerWorld.usuario.keyMap[tecla] == EVENT_down:
                vinerWorld.usuario.keyMap[tecla] = value
                vinerOnline.envia_pacote_server(1, get_acao_por_tecla(tecla), [tecla, value])
            
        else:
            vinerWorld.usuario.keyMap[tecla] = value
            vinerOnline.envia_pacote_server(1, get_acao_por_tecla(tecla), [tecla, value])
                
    def __setKeyCamera(self, key, value):
        vinerWorld.camera.keyMap[key] = value
        
    def __setEventEnter(self):
        msg = vinerDirect.EnviarMsgGeral.etyMsg.get()
                
        if msg == "":            
            if vinerDirect.EnviarMsgGeral.isShowing():
                vinerDirect.EnviarMsgGeral.hide()
            else:
                vinerDirect.EnviarMsgGeral.show()    
            
        
        