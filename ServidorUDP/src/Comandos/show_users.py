'''
Created on 29/04/2011

@author: avner.goncalves
'''

from Abstract.comando import Comando

class ShowUsers(object):
    
    def __init__(self):        
        pass
    
    def mostrar(self):        
        obj_usuario_dic = vinerOnline.get_obj_usuario_on_dic()
    
        total = len(obj_usuario_dic)
        if total > 0:
            for i in obj_usuario_dic:
                print '%s %s %s %s \n' % (i, obj_usuario_dic[i].addr.get_key_addr(), obj_usuario_dic[i].ping, obj_usuario_dic[i].login)
                
            print 'Total: %s' % total
        else:
            print 'Nenhum usuario conectado'
        
class AcaoShowUsers(Comando):
    
    def __init__(self, show_users):
        self.show_users = show_users
        
    def execute(self, *args):        
        self.show_users.mostrar()