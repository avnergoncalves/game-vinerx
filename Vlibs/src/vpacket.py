'''
Created on 16/01/2012

@author: avner.goncalves
'''

import time
from vencrypt import v_encode, v_decode

class vPacket(object):
    '''
    classdocs
    '''

    def __init__(self, endereco, protocolo, sequencia, tipo, acao, args):
        '''
        Constructor
        '''
        self.__time      = time.time()                
        self.__endereco  = endereco        
        self.__protocolo = protocolo
        
        self.sequencia = sequencia
                
        self.__tipo = int(tipo)
        self.__acao = int(acao)
        
        self.__args = args
        
        
              
    @staticmethod
    def instancia_vPacote(data, endereco):
        data = v_decode(data)
        
        protocolo = data[0]
        sequencia = int(data[1])
        tipo      = int(data[2])
        acao      = int(data[3])
        
        args = []        
        for i in range(4, len(data)):
            args.append(data[i])
                
        objvPacket = vPacket(endereco, protocolo, sequencia, tipo, acao, args)
        
        return objvPacket
    
    def set_sequencia(self, sequencia):
        self.sequencia = int(sequencia)
    
    def get_sequencia(self):
        return self.sequencia
    
    def get_endereco(self):
        return self.__endereco
    
    def get_protocolo(self):
        return self.__protocolo
    
    def get_tipo(self):
        return self.__tipo
    
    def get_acao(self):
        return self.__acao
    
    def get_time(self):            
        return self.__time
    
    def get_args(self):            
        return self.__args
    
    def get_arg(self, nro):
        retorno = ""
        
        total = len(self.__args)        
        
        if total > 0 and nro < total: 
            retorno = self.__args[nro]
            
        return retorno        
    
    def get_data(self):
        data = [str(self.__protocolo), str(self.sequencia), str(self.__tipo), str(self.__acao)]
        
        for i in self.__args:
            data.append(str(i))
            
        #data.extend(self.__args)        
        return v_encode(data)
        