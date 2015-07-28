'''
Created on 06/05/2011

@author: avner.goncalves
'''



from Tarefas.recebe_processa_pacotes import ProcessaPacotes
from Tarefas.recebe_processa_comandos import RecebeProcessaComandos
from Tarefas.remove_usuarios import RemoveUsuarios
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
        obj_trf = ProcessaPacotes()
        obj_trf.setHandler(handler)
        
        vAsyncTaskMgr.add(0, .0001, obj_trf.processar, "RecebeProcessaPacotes")    
    
    def _recebe_processa_comandos(self, handler):
        '''
        Cria a tarefa que atenden os comandos no prompt
        '''
        obj_trf = RecebeProcessaComandos()
        obj_trf.setHandler(handler)

        vAsyncTaskMgr.add(0,.1,obj_trf.listen, "RecebeProcessaComandos")
    
    def _remove_usuarios(self):
        '''
        Cria a tarefa que remove os usuarios inativos
        '''
        obj_trf = RemoveUsuarios()
        vAsyncTaskMgr.add(0,.5,obj_trf.remover, "RemoveUsuarios")
        
    def _reenvia_pacotes(self):
        '''
        Cria a tarefa que reenvia os pacotes nao confirmado
        '''
        obj_trf = ReenviaPacotes()
        vAsyncTaskMgr.add(0,.5,obj_trf.executar, "ReenviaPacotes")