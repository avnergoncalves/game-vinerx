'''
Created on 29/04/2011

@author: avner.goncalves
'''

import sys

from Abstract.acao import Acao

from Viner.Helpers.tools import addMensagem

from Configs.cores import COR_VERMELHO

class Desconectar(object):
    
    def __init__(self):        
        pass
    
    def __desconecta_usuario_principal(self, key_usuario):        
        obj_usuario = vinerOnline.busca_usuario_por_key(key_usuario)
        obj_usuario.delete()
                  
        vinerOnline.flg_conectado = vinerOnline.DESCONECT
        print "Voce foi desconectado !!!"
        
        vinerOnline.remove_usuario(key_usuario)
        
        sys.exit()
    
    def __desconecta_usuario(self, key_usuario):        
        
        obj_usuario = vinerOnline.busca_usuario_por_key(key_usuario)
        obj_usuario.delete()
        
        addMensagem(obj_usuario.nick+" foi desconectado !!!", COR_VERMELHO)
        
        vinerOnline.remove_usuario(key_usuario)
        
    def remover_usuario(self, key_usuario):
        if key_usuario == "" or key_usuario == vinerWorld.usuario.key:
            self.__desconecta_usuario_principal(key_usuario)
        else:
            self.__desconecta_usuario(key_usuario)                
        
class AcaoDesconectar(Acao):
    
    def __init__(self, drop_usuario):
        self.drop_usuario = drop_usuario
        
    def execute(self, pacote):
        
        key_usuario = pacote.get_arg(0)
        
        self.drop_usuario.remover_usuario(key_usuario)