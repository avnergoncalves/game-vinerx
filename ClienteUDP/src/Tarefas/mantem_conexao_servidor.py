'''
Created on 06/05/2011

@author: avner.goncalves
'''
import time

from vconstantes import ACAO_SERVER_verificaStatus, LIMIT_DROP_USUARIO

class MantemConexaoServidor(object):
    '''
    ListenComandos
    '''    
    
    def execute(self):
        '''
        Processa pacotes
        '''
        
        if vinerOnline.is_conectado():
            
            vusuario_server = vinerOnline.get_vusuario_server()
            
            if time.time() > vusuario_server.tm_ultimo_pacote_enviado+(LIMIT_DROP_USUARIO*0.33):
                vinerOnline.envia_pacote_server(1, ACAO_SERVER_verificaStatus)                                            