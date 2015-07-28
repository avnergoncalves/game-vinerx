'''
Created on 11/01/2012

@author: avner.goncalves
'''
from socket import gethostbyname

class vAddress(object):        
    
    def __init__(self, addr, port = None):
        '''
        Constructor
        '''
        if type(addr) == tuple:
            self.set_addr(addr)
        else:
            self.set_host(addr)
            self.set_port(port)
            
    def set_host(self, host):
        self.__host = gethostbyname(host)
            
    def get_host(self):
        return self.__host
    
    def set_port(self, port):
        self.__port = int(port)
    
    def get_port(self):
        return self.__port
    
    def set_addr(self, addr):
        host, port = addr
        
        self.set_host(host)
        self.set_port(port)        
    
    def get_addr(self):
        return (self.__host, self.__port)
    
    def get_key_addr(self):
        return self.__host+':'+str(self.__port)