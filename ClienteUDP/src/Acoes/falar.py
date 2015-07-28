'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.acao import Acao

from Viner.Helpers.tools import addMensagem
from Configs.cores import COR_VERMELHO, COR_LARANJA

class Falar(object):
    
    def show(self, mensagem, key_remetente, tipo):
                
        obj_usuario = vinerOnline.busca_usuario_por_key(key_remetente)
        
        if obj_usuario:
            
            if key_remetente != "": 
                mensagem = '%s: %s' % (obj_usuario.nick, mensagem)
            
            #mostra Mensagem usuario
            if tipo == "0":
                addMensagem(mensagem, COR_VERMELHO)
            elif tipo == "1":                                            
                addMensagem(mensagem)
            elif tipo == "2":
                addMensagem(mensagem, COR_LARANJA)
            #mostra Mensagem usuario        
        
class AcaoFalar(Acao):
    
    def __init__(self, falar):
        self.falar = falar
        
    def execute(self, pacote):
        
        mensagem      = pacote.get_arg(0)
        key_remetente = pacote.get_arg(1)
        tipo          = pacote.get_arg(2)
                                            
        self.falar.show(mensagem, key_remetente, tipo)