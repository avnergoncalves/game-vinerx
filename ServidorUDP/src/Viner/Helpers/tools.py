'''
Created on 10/02/2012

@author: avner.goncalves
'''
from vconstantes import ACAO_CLIENT_POR_TECLA

def get_path_modelo(nome_modelo):
    from pandac.PandaModules import Filename
    import sys
    
    winfile = sys.path[0]+"\\Modelos\\"+nome_modelo
    pandafile = Filename.fromOsSpecific(winfile)
    
    return pandafile

def get_acao_por_tecla(tecla):
    return ACAO_CLIENT_POR_TECLA[tecla]