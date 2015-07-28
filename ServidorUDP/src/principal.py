'''
Created on 01/03/2011

@author: avner.goncalves
'''
import sys, os

sys.path.append("C:\\Workspace Python\\[Viner]vlibs\\src")

from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
loadPrcFileData("", "window-type none")
loadPrcFileData("", "audio-library-name null")
loadPrcFileData("", "client-sleep 0.001")

from vthread import vThread

from vconstantes import ACAO_confirmarPacote, ACAO_SERVER_conectar, ACAO_SERVER_desconectar, \
    ACAO_SERVER_recuperarUsuariosOnline, ACAO_SERVER_mover, ACAO_SERVER_rodar, ACAO_SERVER_falar, \
    ACAO_SERVER_verificaStatus

from Viner.viner_online import VinerOnline
from Viner.viner_world import VinerWorld

from Tarefas.factory_tarefas import FactoryTarefas

#Imports Acoes
from Acoes.handler_acoes import HandlerAcoes

from Acoes.conectar import Conectar, AcaoConectar

from Acoes.confirmar_pacote import ConfirmarPacote, AcaoConfirmarPacote
from Acoes.desconetar import Desconectar, AcaoDesconectar
from Acoes.verifica_status import VerificaStatus, AcaoVerificaStatus

from Acoes.envia_dados_usuarios_online import EnviaDadosUsuariosOnline, AcaoEnviaDadosUsuariosOnline
from Acoes.mover import Mover, AcaoMover
from Acoes.rodar import Rodar, AcaoRodar
from Acoes.falar import Falar, AcaoFalar
#Imports Acoes

#Imports Comandos
from Comandos.handler_comandos import HandlerComandos

from Comandos.exit import Exit, AcaoExit
from Comandos.clear import Clear, AcaoClear
from Comandos.show_users import ShowUsers, AcaoShowUsers
from Comandos.show_threads import ShowTreads, AcaoShowTreads
#Imports Comandos

from Viner.Libs.World.usuario import Usuario

class Principal(ShowBase):
    def __init__(self):
        '''
        Instacia os objetos mais importantes
        '''
        ShowBase.__init__(self)
        
        __builtins__.vAsyncTaskMgr = vThread()
        __builtins__.vinerOnline   = VinerOnline()
        __builtins__.vinerWorld    = VinerWorld()            
        
        self.__factory_tarefas     = FactoryTarefas()
        
        self.__handler_action      = HandlerAcoes()
        self.__handler_comand      = HandlerComandos()
    
    def __carrega_usuarios(self):
        print 'Carregando Usuarios... '
        obj_usuario1                  = Usuario()
        obj_usuario1.login            = 'viner'
        obj_usuario1.senha            = 'viner'        
        obj_usuario1.nick             = 'Viner'
        obj_usuario1.vida_real        = 100
        obj_usuario1.vida_total       = 100
        obj_usuario1.mana_real        = 100
        obj_usuario1.mana_total       = 100        
        obj_usuario1.forca            = 1000
        obj_usuario1.velocidade       = 30
        obj_usuario1.velocidade_atack = 15        
        
        obj_usuario2                  = Usuario()
        obj_usuario2.login            = 'teste1'
        obj_usuario2.senha            = 'teste1'
        obj_usuario2.nick             = 'Teste 1'
        obj_usuario2.vida_real        = 100
        obj_usuario2.vida_total       = 100
        obj_usuario2.mana_real        = 100
        obj_usuario2.mana_total       = 100        
        obj_usuario2.forca            = 1000
        obj_usuario2.velocidade       = 30
        obj_usuario2.velocidade_atack = 15        
        
        obj_usuario3                  = Usuario()
        obj_usuario3.login            = 'teste2'
        obj_usuario3.senha            = 'teste2'
        obj_usuario3.nick             = 'Teste 2'
        obj_usuario3.vida_real        = 100
        obj_usuario3.vida_total       = 100
        obj_usuario3.mana_real        = 100
        obj_usuario3.mana_total       = 100
        obj_usuario3.forca            = 1000
        obj_usuario3.velocidade       = 5
        obj_usuario3.velocidade_atack = 15
        
        vinerOnline.add_obj_usuario_off_dic(obj_usuario1)
        vinerOnline.add_obj_usuario_off_dic(obj_usuario2)
        vinerOnline.add_obj_usuario_off_dic(obj_usuario3)
        print '[OK]'
        
        
    def __carrega_handler(self):
        '''
        Carrega todas acoes e comandos
        acoes: Tudo que um cliente consegue fazer
        comandos: Executados em linha de comando no servidor
        '''            
        
        print 'Carregando Acoes Publicas... '                
        acao_conectar = AcaoConectar( Conectar() )
        self.__handler_action.set_acoes_publicas(ACAO_SERVER_conectar, acao_conectar)
        print '[OK]'
        
        print 'Carregando Acoes Privadas... '
        acao_confirmar_pacote = AcaoConfirmarPacote( ConfirmarPacote() )
        self.__handler_action.set_acoes_privadas(ACAO_confirmarPacote, acao_confirmar_pacote)
        
        acao_desconectar = AcaoDesconectar( Desconectar() )
        self.__handler_action.set_acoes_privadas(ACAO_SERVER_desconectar, acao_desconectar)
        
        acao_verifica_status = AcaoVerificaStatus( VerificaStatus() )
        self.__handler_action.set_acoes_privadas(ACAO_SERVER_verificaStatus, acao_verifica_status)
        
        acao_envia_dados_usuarios_online = AcaoEnviaDadosUsuariosOnline( EnviaDadosUsuariosOnline() )
        self.__handler_action.set_acoes_privadas(ACAO_SERVER_recuperarUsuariosOnline, 
                                                 acao_envia_dados_usuarios_online)            
        
        acao_mover = AcaoMover( Mover() )
        self.__handler_action.set_acoes_privadas(ACAO_SERVER_mover, acao_mover)
        
        acao_rodar = AcaoRodar( Rodar() )
        self.__handler_action.set_acoes_privadas(ACAO_SERVER_rodar, acao_rodar)             
        
        acao_falar = AcaoFalar( Falar() )
        self.__handler_action.set_acoes_privadas(ACAO_SERVER_falar, acao_falar)            
        print '[OK]'
        
        print 'Carregando Comandos... '
        comando_exit = AcaoExit( Exit() )
        self.__handler_comand.set_comando('exit', comando_exit)
        
        comando_clear = AcaoClear( Clear() )
        self.__handler_comand.set_comando('clear', comando_clear)
        
        comando_show_users = AcaoShowUsers( ShowUsers() )
        self.__handler_comand.set_comando('show_users', comando_show_users)
        
        comando_show_treads = AcaoShowTreads( ShowTreads() )
        self.__handler_comand.set_comando('show_threads', comando_show_treads)
        print '[OK]'
        
        #Limpa a Tela
        os.system('cls')
    
    
    def __carrega_tarefas(self):
        self.__factory_tarefas.cria_tarefa('recebe_processa_pacotes', self.__handler_action)
            
        self.__factory_tarefas.cria_tarefa('recebe_processa_comandos', self.__handler_comand)
            
        self.__factory_tarefas.cria_tarefa('remove_usuarios')
            
        self.__factory_tarefas.cria_tarefa('reenvia_pacotes')
    
    def iniciar(self):
        '''
        Inicia o servidor e cria as tarefas
        '''
        if vinerOnline.startup():
            
            self.__carrega_usuarios()
            
            self.__carrega_handler()
            
            self.__carrega_tarefas()
            
            vAsyncTaskMgr.iniciar()                    
            
            self.run()
        else:
            print 'Ocorreu algum erro ao tentar iniciar o Servidor'
        
p1 = Principal()
p1.iniciar()