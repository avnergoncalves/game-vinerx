'''
Created on 08/02/2012

@author: viner
'''
from direct.gui.DirectGui import DirectFrame, DirectEntry, DirectLabel, DirectButton, DGG
from Viner.Helpers.tools import addMensagem

from Configs.config import TENTATIVAS, INTERVALO_TENTATIVAS
from Configs.cores import COR_BRANCO, COR_VERMELHO

class FrameAutenticacao(object):
    '''
    FrameAutenticacao
    '''

    def __init__(self, parent = None, **kw):
        self.__qtd_conexao = 0        
        
        self.__frmAuth = DirectFrame( frameColor = (0,0,0,.3),
                                      frameSize  = (-.5,.5,0,0.45), 
                                      pos        = (0,0,-.1),                                      
                                      enableEdit = 1 )        
        
        self.__lblLogin = DirectLabel( text       = "Login: ",
                                       scale      = 0.05,
                                       pos        = (-0.3, 0, 0.3),
                                       frameColor = (0,0,0,0),
                                       text_fg    = (1,1,1,1) )
            
        self.__etyLogin = DirectEntry( scale      = 0.05,
                                       width      = 12,                                       
                                       pos        = (-0.2, 0, 0.3),
                                       cursorKeys = 1,
                                       focus      = 1, )        
                
        self.__lblSenha = DirectLabel( text       = "Senha: ",
                                       scale      = 0.05,
                                       pos        = (-0.3, 0, 0.2),
                                       frameColor = (0,0,0,0),
                                       text_fg    = (1,1,1,1) )        
        
        self.__etySenha = DirectEntry( scale          = 0.05,
                                       width          = 12,                                       
                                       pos            = (-.2, 0, 0.2),
                                       cursorKeys     = 1, 
                                       obscured       = 1,                                    
                                       focusInCommand = self.__command_clear_senha)
        
        
        self.__btnEntrar = DirectButton( frameColor    = (0,0,0,1),
                                         text          = "Entrar",
                                         scale         = 0.06,                                                                                
                                         pos           = (0.3, 0, 0.1),
                                         text_fg       = (1,1,1,1),                                                                                   
                                         rolloverSound = None,
                                         clickSound    = None,
                                         command       = self.__command_entrar)
        
        self.__lblLogin.reparentTo(self.__frmAuth)
        self.__etyLogin.reparentTo(self.__frmAuth)
        self.__lblSenha.reparentTo(self.__frmAuth)
        self.__etySenha.reparentTo(self.__frmAuth)        
        self.__btnEntrar.reparentTo(self.__frmAuth)
        
        self.__etyLogin.set("viner")
        self.__etySenha.set("viner")
    
    def __command_clear_senha(self):
        self.__etySenha.set("")
    
    def __command_entrar(self, txt = None):                
        login = self.__etyLogin.get()
        senha = self.__etySenha.get()
                
        valido = True
        
        if login == "":
            addMensagem("O campo Login e obrigatorio !", COR_BRANCO)
            valido = False
            
        if senha == "":
            addMensagem("O campo Senha e obrigatorio !", COR_BRANCO)
            valido = False
        
        if valido:
            self.__btnEntrar["state"] = DGG.DISABLED
                        
            taskMgr.add( self.__task_conectar_servidor,
                         'ConectarServidor',
                          extraArgs=[login,senha],
                          appendTask=True)                            
            
            #inicia_nova_thread(1, 0, "Conectar Servidor", self.__conectar_servidor, login, senha)
                        
    def __task_conectar_servidor(self, login, senha, task):            
                
        if self.__qtd_conexao < TENTATIVAS:                                        
            
            if vinerOnline.flg_conectado == vinerOnline.ERROLOGIN:
                vinerOnline.flg_conectado = vinerOnline.DESCONECT
                
                self.__btnEntrar["state"] = DGG.NORMAL
                self.__qtd_conexao        = 0
                                
                addMensagem('Login ou senha invalido', COR_VERMELHO)
                
                self.__etyLogin.setFocus()
                                
            elif vinerOnline.flg_conectado == vinerOnline.CONECTADO:
                #addMensagem("Conectado 12 !!!")
                #self.destroy()
                pass
                
            else:
                vinerOnline.conectar_servidor(login, senha)
                self.__qtd_conexao += 1
                
                taskMgr.doMethodLater( INTERVALO_TENTATIVAS,
                                   self.__task_conectar_servidor, 
                                   'ConectarServidorLater',
                                   extraArgs = [login,senha],
                                   appendTask = True)
                
                msg = "Tentativa %s/5 -  Conectando..." % (self.__qtd_conexao)
                addMensagem(msg, COR_BRANCO)                                            
                
        else:
            vinerOnline.flg_conectado = vinerOnline.DESCONECT
            self.__btnEntrar["state"] = DGG.NORMAL
            self.__qtd_conexao        = 0            
            addMensagem("Servidor nao encontrado", COR_VERMELHO)                        
            
        
        return task.done
        
    def destroy(self):        
        self.__frmAuth.destroy()
        
        del self.__lblLogin
        del self.__etyLogin
        del self.__lblSenha
        del self.__etySenha        
        del self.__btnEntrar
        del self.__frmAuth
            