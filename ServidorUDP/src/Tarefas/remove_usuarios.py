'''
Created on 25/01/2011

@author: avner.goncalves
'''

import time
from vconstantes import LIMIT_DROP_USUARIO

class RemoveUsuarios(object):
    '''    
    '''        
        
    def remover(self):
        '''        
        '''                    
        vusuarios = vinerOnline.get_dic_vusuarios()
        
        for key_addr in vusuarios:            
            if time.time() > vusuarios[key_addr].tm_ultimo_pacote_recebido+LIMIT_DROP_USUARIO:                                                                        
                vinerOnline.remove_usuario(key_addr)
                print '%s desconectado por TimeOut' % key_addr