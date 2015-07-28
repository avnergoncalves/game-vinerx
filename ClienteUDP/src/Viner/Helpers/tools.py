'''
Created on 10/02/2012

@author: avner.goncalves
'''

import sys

from pandac.PandaModules import Filename

from vconstantes import ACAO_SERVER_POR_TECLA

from Configs.cores import COR_BRANCO

def addMensagem(texto, cor = COR_BRANCO):
    return vinerDirect.FrameMsgGeral.show(texto, cor)

def render_graphics():
    base.graphicsEngine.renderFrame()
    base.graphicsEngine.renderFrame()

def get_path_animacao(nome_modelo):
    winfile = sys.path[0]+"\\Modelos\\"+nome_modelo
    pandafile = Filename.fromOsSpecific(winfile)
    
    return pandafile

def get_path_modelo(nome_modelo):
    winfile = sys.path[0]+"\\Modelos\\"+nome_modelo
    pandafile = Filename.fromOsSpecific(winfile)
    
    return pandafile

def hidden_mouse(flg):
    vinerProps.setCursorHidden(flg)
    base.win.requestProperties(vinerProps)
    
def get_acao_por_tecla(tecla):
    return ACAO_SERVER_POR_TECLA[tecla]