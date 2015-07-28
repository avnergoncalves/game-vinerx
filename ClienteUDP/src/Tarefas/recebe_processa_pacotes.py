'''
Created on 06/05/2011

@author: avner.goncalves
'''
import time

class RecebeProcessaPacotes(object):
    '''
    ListenComandos
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__handler  = None   
        self.__qtd      = 0
        self.__priority = 0     
    
    def setHandler(self, handler):
        '''
        Seta o manipulador de comandos
        '''
        self.__handler = handler        
    
    def __remove_processo(self, task):
        self.__qtd -= 1
    
    def __cria_processo(self, pacote):        
        
        if self.__qtd == 0:
            self.__priority = 0
        else:
            self.__priority -= 1             
        
        self.__qtd += 1
        
        taskMgr.add(self.__handler.execute_acao,'Sub-RecebeProcessaPacotes',sort=4,priority=self.__priority,extraArgs=[pacote],appendTask=True,uponDeath=self.__remove_processo)
        #taskMgr.add(self.__handler.execute_acao,'Sub-RecebeProcessaPacotes',sort=4,extraArgs=[pacote],appendTask=True,uponDeath=self.__remove_processo)
    
    def processar(self):
        '''
        Processa pacotes
        '''                        
        try:
            if vinerOnline.flg_conectado != vinerOnline.DESCONECT:
                pacote = vinerOnline.recebe_pacote()
            
                if pacote:
                    self.__cria_processo(pacote)
                    
            else:
                time.sleep(0.1)
        except:
                print 'Erro ReceberPacotes'