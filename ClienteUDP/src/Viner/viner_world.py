'''
Created on 09/02/2012

@author: viner
'''

from Viner.Libs.World.mapa import Mapa
from Viner.Libs.World.usuario import Usuario
from Viner.Libs.World.comunicacao import Comunicacao
from Viner.Libs.World.camera import Camera 
from Viner.Libs.World.evento import Evento

from Viner.Helpers.tools import render_graphics

class VinerWorld(object):
    '''
    '''

    def __init__(self):
        '''
        '''
        self.mapa        = None
        self.usuario     = None
        self.comunicacao = None
        self.camera      = None
        self.evento      = None
        
    def carregar(self, dadosUsuario):
        #mostra a barra de progresso
        vinerDirect.ProgressBar.show()
        #mostra a barra de progresso
        
        #autaliza os objetos na tela         
        render_graphics()
        #autaliza os objetos na tela
        
        #Carrega mapa
        self.mapa = Mapa()
        #Carrega mapa
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(10)
        #atualiza a barra de progresso
                        
        #Carrega usuario principal
        self.usuario = Usuario(dadosUsuario, True)
        vinerOnline.registra_usuario(self.usuario)
        #Carrega usuario principal
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(20)
        #atualiza a barra de progresso
        
        self.evento = Evento()
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(30)
        #atualiza a barra de progresso
                
        self.comunicacao = Comunicacao()
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(40)
        #atualiza a barra de progresso
                    
        self.camera = Camera()
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(50)
        #atualiza a barra de progresso
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(60)
        #atualiza a barra de progresso
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(70)
        #atualiza a barra de progresso
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(80)
        #atualiza a barra de progresso
        
        #atualiza a barra de progresso
        vinerDirect.ProgressBar.update(90)
        #atualiza a barra de progresso
                
        #finaliza a barra de progresso
        vinerDirect.ProgressBar.finish()
        #finaliza a barra de progresso
        
        
    def carregarUsuario(self, dadosUsuario, principal = False):        
        usuario = Usuario(dadosUsuario, principal)
        vinerOnline.registra_usuario(usuario)
        
        return usuario
        