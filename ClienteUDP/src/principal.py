'''
Created on 15/03/2011

@author: avner.goncalves
'''
import sys

sys.path.append("C:\\Workspace Python\\[Viner]vlibs\\src")

from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import WindowProperties

from panda3d.core import loadPrcFileData
loadPrcFileData("", "audio-library-name null")
loadPrcFileData("", "client-sleep 0.001")

from vthread import vThread

from vconstantes import ACAO_confirmarPacote, ACAO_CLIENT_conectar, ACAO_CLIENT_desconectar,\
    ACAO_CLIENT_mover, ACAO_CLIENT_rodar, ACAO_CLIENT_falar

#Importa Global's Class's
from Viner.viner_online import VinerOnline
from Viner.viner_direct import VinerDirect
from Viner.viner_world import VinerWorld

#Importa Acoes
from Acoes.handler_acoes import HandlerAcoes

from Acoes.conectar import Conectar, AcaoConectar

from Acoes.confirmar_pacote import ConfirmarPacote, AcaoConfirmarPacote
from Acoes.desconetar import Desconectar, AcaoDesconectar
from Acoes.mover import Mover, AcaoMover
from Acoes.rodar import Rodar, AcaoRodar
from Acoes.falar import Falar, AcaoFalar

#importa Tarefas
from Tarefas.factory_tarefas import FactoryTarefas

class Viner(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        
        #Desabilita o Mouse
        base.disableMouse()
        
        __builtins__.vAsyncTaskMgr = vThread()
        __builtins__.vinerProps    = WindowProperties()
        __builtins__.vinerOnline   = VinerOnline()
        __builtins__.vinerDirect   = VinerDirect()
        __builtins__.vinerWorld    = VinerWorld()        

        self.__handler_acoes   = HandlerAcoes()
        self.__factory_tarefas = FactoryTarefas()

    def __carrega_acoes(self):
        
        #Acoes publicas
        acao_conectar = AcaoConectar( Conectar() )
        self.__handler_acoes.set_acoes_publicas(ACAO_CLIENT_conectar, acao_conectar)
        #Acoes publicas
        
        #Acoes privadas
        acao_confirmar_pacote = AcaoConfirmarPacote( ConfirmarPacote() )
        self.__handler_acoes.set_acoes_privadas(ACAO_confirmarPacote, acao_confirmar_pacote)
        
        acao_desconectar = AcaoDesconectar( Desconectar() )
        self.__handler_acoes.set_acoes_privadas(ACAO_CLIENT_desconectar, acao_desconectar)                            
        
        acao_mover = AcaoMover( Mover() )
        self.__handler_acoes.set_acoes_privadas(ACAO_CLIENT_mover, acao_mover)
        
        acao_rodar = AcaoRodar( Rodar() )
        self.__handler_acoes.set_acoes_privadas(ACAO_CLIENT_rodar, acao_rodar)            
        
        acao_falar = AcaoFalar( Falar() )
        self.__handler_acoes.set_acoes_privadas(ACAO_CLIENT_falar, acao_falar)            
        #Acoes privadas
        
    def __carrega_tarefas(self):            
        
        self.__factory_tarefas.cria_tarefa('recebe_processa_pacotes', self.__handler_acoes)            
        
        self.__factory_tarefas.cria_tarefa('mantem_conexao_servidor')
        
        self.__factory_tarefas.cria_tarefa('reenvia_pacotes')

    def iniciar(self):
        
        self.__carrega_acoes()
                
        self.__carrega_tarefas()
        
        vAsyncTaskMgr.iniciar()
        
        self.run()

app = Viner()
app.iniciar()