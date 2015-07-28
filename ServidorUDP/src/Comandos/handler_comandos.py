'''
Created on 29/04/2011

@author: avner.goncalves
'''
class HandlerComandos(object):
    
    def __init__(self):
        self.comandos = {}        
    
    def set_comando(self, key, comando):
        self.comandos.update({key:comando})
    
    def show_comandos(self):
        for key in self.comandos:
            print 'Comando: [%s] Objeto: %s \n' % (key, self.comandos[key])
        
    def execute_comando(self, comando):
        
        params = comando.split(' ')
        
        evento = params.pop(0)
        
        if self.comandos.has_key(evento):                                                      
            self.comandos.get(evento).execute(params)
        else:
            print '\'%s\' nao eh um comando valido \n' % evento
            self.show_comandos()
        
            
    