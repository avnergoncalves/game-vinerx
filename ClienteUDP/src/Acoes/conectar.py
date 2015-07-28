'''
Created on 29/04/2011

@author: avner.goncalves
'''

from vconstantes import ACAO_SERVER_recuperarUsuariosOnline, RESPOSTA_USU_PRINCIPAL_CONECTADO,\
                        RESPOSTA_USU_NOVO_CONECTADO, RESPOSTA_DADOS_INVALIDO

from Abstract.acao import Acao

from Viner.Helpers.tools import addMensagem


class Conectar(object):

    def carrega_usuario_principal(self, dadosUsuario):
        
        if vinerOnline.flg_conectado != vinerOnline.CONECTADO:
            
            vinerOnline.flg_conectado = vinerOnline.CONECTADO
            vinerOnline.key           = dadosUsuario['key']
            
            #mostra msg conectado
            addMensagem("Conectado !!!")
            
            #remove o painel de autenticacao
            vinerDirect.FrameAutenticacao.destroy()
            
            #carrega o mundo
            vinerWorld.carregar(dadosUsuario)
            
            #requisita usuarios online
            vinerOnline.envia_pacote_server(0, ACAO_SERVER_recuperarUsuariosOnline)

    def carrega_usuario_novo(self, dadosUsuario):        
        usuario = vinerOnline.busca_usuario_por_key(dadosUsuario['key'])
        if not usuario: 
            vinerWorld.carregarUsuario(dadosUsuario)

    def erro_login_senha(self):
        #print 'Login ou senha invalida'
        vinerOnline.flg_conectado = vinerOnline.ERROLOGIN
                        
class AcaoConectar(Acao):
    
    def __init__(self, conectar_usuario):
        self.conectar_usuario = conectar_usuario
    
    def __get_dados_usuario(self, pacote):
        dadosUsuario = {}
    
        dadosUsuario['key']              = pacote.get_arg(1)
        dadosUsuario['nick']             = pacote.get_arg(2)
        dadosUsuario['vida_real']        = pacote.get_arg(3)
        dadosUsuario['vida_total']       = pacote.get_arg(4)
        dadosUsuario['mana_real']        = pacote.get_arg(5)
        dadosUsuario['mana_total']       = pacote.get_arg(6)
        dadosUsuario['forca']            = pacote.get_arg(7)
        dadosUsuario['velocidade']       = pacote.get_arg(8)
        dadosUsuario['velocidade_atack'] = pacote.get_arg(9)            
        dadosUsuario['x']                = pacote.get_arg(10)
        dadosUsuario['y']                = pacote.get_arg(11)
        dadosUsuario['z']                = pacote.get_arg(12)
        dadosUsuario['h']                = pacote.get_arg(13)
        
        return dadosUsuario 
    
    def execute(self, pacote):

        retorno_server = pacote.get_arg(0)
        
        if retorno_server == RESPOSTA_USU_PRINCIPAL_CONECTADO:
            dadosUsuario = self.__get_dados_usuario(pacote)            
            
            self.conectar_usuario.carrega_usuario_principal(dadosUsuario)
            
        elif retorno_server == RESPOSTA_USU_NOVO_CONECTADO:
            dadosUsuario = self.__get_dados_usuario(pacote)                        
            
            self.conectar_usuario.carrega_usuario_novo(dadosUsuario)
            
        elif retorno_server == RESPOSTA_DADOS_INVALIDO:
            self.conectar_usuario.erro_login_senha()