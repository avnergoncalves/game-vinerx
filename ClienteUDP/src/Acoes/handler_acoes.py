'''
Created on 29/04/2011

@author: avner.goncalves
'''
class HandlerAcoes(object):
    
    def __init__(self):
        self.acoes_publicas = {}
        self.acoes_privadas = {}                
    
    def set_acoes_publicas(self, key, acao):
        self.acoes_publicas.update({key:acao})
        
    def set_acoes_privadas(self, key, acao):
        self.acoes_privadas.update({key:acao})
        
    def execute_acao(self, pacote, task):
        
        fluxo = vinerOnline.controle_fluxo(pacote)            
        
        if fluxo == vinerOnline.ALLOWED:
                        
            acao = pacote.get_acao()

            if  self.acoes_publicas.has_key(acao):            
                self.acoes_publicas.get(acao).execute(pacote)
                
            elif self.acoes_privadas.has_key(acao):
                self.acoes_privadas.get(acao).execute(pacote)
                                                
            else:
                print "Nao existe essa acao"
                
        elif fluxo == vinerOnline.DENIED:
            print "DENIED"        
        elif fluxo == vinerOnline.PASSED:
            print "PASSED"
            
        return task.done