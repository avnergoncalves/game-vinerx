'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.comando import Comando
from vthread import inicia_nova_thread

class ShowTreads(object):
    
    def __init__(self):        
        pass        
    
    def mostrar(self):        
        val_tarefa_dic = vAsyncTaskMgr.get()
    
        total = len(val_tarefa_dic)
        if total > 0:
            for nome in val_tarefa_dic:
                count = val_tarefa_dic[nome].get_count()
                delay = val_tarefa_dic[nome].get_delay()
                funcao = val_tarefa_dic[nome].get_funcao()
                            
                print '%s %s %s %s \n' % ( count, delay, nome, funcao)
                
            print 'Total: %s' % total
        else:
            print 'Nenhum tarefa em execucao'
        
class AcaoShowTreads(Comando):
    
    def __init__(self, show_ports):
        self.show_ports = show_ports
        
    def execute(self, *args):                
        self.show_ports.mostrar()