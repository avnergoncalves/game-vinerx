'''
Created on 06/05/2011

@author: avner.goncalves
'''

from Tarefas.recebe_processa_pacotes import RecebeProcessaPacotes
from Tarefas.mantem_conexao_servidor import MantemConexaoServidor
from Tarefas.reenvia_pacotes import ReenviaPacotes

class FactoryTarefas(object):
    '''
    Fabrica de taredas, onde cria as tarefas
    '''        
    
    def cria_tarefa(self, tarefa, *args):
        '''
        Cria as tarefas
        '''        
        tarefa = '_'+tarefa
        
        if hasattr(self, tarefa): 
            func = getattr(self, tarefa)
            func(*args)            
    
    def _recebe_processa_pacotes(self, handler):
        obj_trf = RecebeProcessaPacotes()
        obj_trf.setHandler(handler)
        
        vAsyncTaskMgr.add(0, .0001, obj_trf.processar, "RecebeProcessaPacotes")    
            
    def _mantem_conexao_servidor(self):        
        obj_trf = MantemConexaoServidor()
        
        vAsyncTaskMgr.add(0, .5, obj_trf.execute, "MantemConexaoServidor")
        
    def _reenvia_pacotes(self):
        '''
        Cria a tarefa que reenvia os pacotes nao confirmado
        '''
        obj_trf = ReenviaPacotes()
        vAsyncTaskMgr.add(0,.5,obj_trf.executar, "ReenviaPacotes")