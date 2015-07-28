'''
Created on 15/03/2011

@author: avner.goncalves
'''
import uuid

from Configs.config import HOST, PORTA

from vsocket import vSocket

from vconstantes import ACAO_CLIENT_desconectar

class VinerOnline(vSocket):
    '''
    ServidorUDP
    '''

    def __init__(self):
        '''
        __init__
        '''        
        vSocket.__init__(self)
        self.bind((HOST, PORTA))
        
        #self.setblocking(False)
        
        self.__conectado = False
        self.__default_socket = None                    
            
        self.__obj_usuario_off_dic      = {}
                
        self.__obj_key_usuario_on_dic   = {}
        self.__idx_addr_usuario_on_dic  = {}
        self.__idx_login_usuario_on_dic = {}
    
    def is_connected(self):
        return self.__conectado                
    
    def add_obj_usuario_off_dic(self, obj_usuario):
        login = obj_usuario.login.lower()
        self.__obj_usuario_off_dic.update({login: obj_usuario});
        
    def add_obj_usuario_on(self, obj_usuario):        
        self.__idx_addr_usuario_on_dic.update({obj_usuario.addr.get_key_addr(): obj_usuario.key})
        
        login = obj_usuario.login.lower()
        self.__idx_login_usuario_on_dic.update({login: obj_usuario.key})
        
        self.__obj_key_usuario_on_dic.update({obj_usuario.key: obj_usuario})
                
    def __pop_obj_usuario_on(self, addr):
        key         = self.__idx_addr_usuario_on_dic.pop(addr)
        obj_usuario = self.__obj_key_usuario_on_dic.pop(key)
        
        self.__idx_login_usuario_on_dic.pop(obj_usuario.login)
        
        return obj_usuario    
    
    def get_dic_vusuarios(self):
        return self.recupera_vusuario().copy()
    
    def get_obj_usuario_off_dic(self):
        return self.__obj_usuario_off_dic.copy()
    
    def get_obj_usuario_on_dic(self):
        return self.__obj_key_usuario_on_dic.copy()
    
    def __get_idx_addr_usuario_on_dic(self):
        return self.__idx_addr_usuario_on_dic.copy()
    
    def __get_copy_idx_login_usuario_on_dic(self):
        return self.__idx_login_usuario_on_dic.copy()
    
    def remove_usuario(self, key_addr):            
        key = self.__idx_addr_usuario_on_dic.get(key_addr)                        
        
        if key:        
            if self.__idx_addr_usuario_on_dic.has_key(key_addr) and self.__obj_key_usuario_on_dic.has_key(key):
                self.envia_pacote_todos(0, ACAO_CLIENT_desconectar, [key])
                                                                  
                obj_usuario_temp = self.__pop_obj_usuario_on(key_addr)
                
                obj_usuario_temp.stop_task_movimentacao()
                
                self.add_obj_usuario_off_dic(obj_usuario_temp)
                
        self.remove_vusuario(key_addr)
                                                            
    def registra_usuario(self, endereco, login):
        key = uuid.uuid4().get_hex()
        
        if not self.__obj_key_usuario_on_dic.has_key(key):
            obj_usuario = self.__obj_usuario_off_dic.pop(login)
                                                            
            obj_usuario.key    = key
            obj_usuario.addr   = endereco
            obj_usuario.login  = login
                        
            obj_usuario.inicia_task_movimentacao()
            
            self.add_obj_usuario_on(obj_usuario)
        else :
            print 'UUID igual em registra_usuario'
            obj_usuario = None
                
        return obj_usuario                                        
    
    def busca_usuario_off_por_login(self, login):
        obj_usuario = None
        
        login = login.lower()
        
        obj_usuario_off_dic = self.get_obj_usuario_off_dic()
        if obj_usuario_off_dic.has_key(login):
            obj_usuario = obj_usuario_off_dic.get(login)
                
        return obj_usuario    
    
    def busca_usuario_on_por_key(self, key):        
        obj_usuario = None
        
        obj_usuario_dic = self.get_obj_usuario_on_dic()
        
        if obj_usuario_dic.has_key(key):
            obj_usuario = obj_usuario_dic.get(key)
                                    
        return obj_usuario
    
    def busca_usuario_on_por_addr(self, key_addr):
        obj_usuario = None
        
        idx_addr_usuario_dic = self.__get_idx_addr_usuario_on_dic() 
        
        if idx_addr_usuario_dic.has_key(key_addr):       
            key = idx_addr_usuario_dic.get(key_addr)
            
            obj_usuario = self.busca_usuario_on_por_key(key)        
                          
        return obj_usuario    
    
    def busca_usuario_on_por_login(self, login):
        obj_usuario = None
        
        login = login.lower()
        
        idx_login_usuario_dic = self.__get_copy_idx_login_usuario_on_dic()
        
        if idx_login_usuario_dic.has_key(login):
            key = idx_login_usuario_dic.get(login)            
            obj_usuario = self.busca_usuario_on_por_key(key)
                                                    
        return obj_usuario
    
    def startup(self):
        if not self.is_connected():                                
            self.__conectado = True
        
        return self.__conectado                
    
    def iniciar_tarefas(self):
        self.__obj_vthread.iniciar()
                                
    def shutdown(self):
        if self.is_connected():                    
            
            self.__obj_vthread.stop()                                

            self.close()
            
            self.__conectado = False    
            
    def envia_pacote_todos(self, tipo, acao, args, excessao = None, habilitado = True):
        obj_usuario_dic = self.get_obj_usuario_on_dic()
        
        if len(obj_usuario_dic) > 0:
            if excessao:
                for i in obj_usuario_dic:
                    if i not in excessao and obj_usuario_dic[i].habilitado == habilitado:                                        
                        self.envia_pacote(obj_usuario_dic[i].addr, tipo, acao, args)
            else:
                for i in obj_usuario_dic:
                    if obj_usuario_dic[i].habilitado == habilitado:
                        self.envia_pacote(obj_usuario_dic[i].addr, tipo, acao, args)                    
            