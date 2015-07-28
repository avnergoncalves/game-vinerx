'''
Created on 16/02/2012

@author: avner.goncalves
'''

'''CONFIGS'''
LIMIT_PKT_POR_SEG  = 30   #unidades/segundos
MAX_SEQUENCE       = 1000 #unidades
LIMIT_DROP_USUARIO = 10   #segundos (minimo 10)
'''CONFIGS'''

'''KEYS'''
TECLA_nenhuma  = "0"
TECLA_esquerda = "1" #teclado letra A
TECLA_direita  = "2" #teclado letra D
TECLA_frente   = "3" #teclado letra W
TECLA_traz     = "4" #teclado letra S
'''KEYS'''

'''EVENT KEYS'''
EVENT_nenhum = "0" 
EVENT_down   = "1"
EVENT_up     = "2" #teclado letra A
'''EVENT KEYS'''


'''RESPOSTAS SERVIDOR'''
RESPOSTA_USU_PRINCIPAL_CONECTADO = "0"
RESPOSTA_USU_NOVO_CONECTADO      = "1"
RESPOSTA_DADOS_INVALIDO          = "2"
'''RESPOSTAS SERVIDOR'''

'''ACOES'''
ACAO_confirmarPacote = 0
'''ACOES'''


'''ACOES SERVIDOR'''
ACAO_SERVER_conectar = 1
ACAO_SERVER_desconectar = 2
ACAO_SERVER_verificaStatus = 3
ACAO_SERVER_recuperarUsuariosOnline = 4
ACAO_SERVER_mover = 5
ACAO_SERVER_rodar = 6
ACAO_SERVER_falar = 7
'''ACOES SERVIDOR'''

'''ACOES SERVIDOR POR TECLA'''
ACAO_SERVER_POR_TECLA = {}
ACAO_SERVER_POR_TECLA.update({TECLA_frente:ACAO_SERVER_mover})
ACAO_SERVER_POR_TECLA.update({TECLA_traz:ACAO_SERVER_mover})
ACAO_SERVER_POR_TECLA.update({TECLA_esquerda:ACAO_SERVER_rodar})
ACAO_SERVER_POR_TECLA.update({TECLA_direita:ACAO_SERVER_rodar})        
'''ACOES SERVIDOR POR TECLA'''


'''ACOES CLIENTE'''
ACAO_CLIENT_conectar = 1
ACAO_CLIENT_desconectar = 2
ACAO_CLIENT_mover = 3
ACAO_CLIENT_rodar = 4
ACAO_CLIENT_falar = 5
'''ACOES CLIENTE'''

'''ACOES CLIENTE POR TECLA'''
ACAO_CLIENT_POR_TECLA = {}
ACAO_CLIENT_POR_TECLA.update({TECLA_frente:ACAO_CLIENT_mover})
ACAO_CLIENT_POR_TECLA.update({TECLA_traz:ACAO_CLIENT_mover})
ACAO_CLIENT_POR_TECLA.update({TECLA_esquerda:ACAO_CLIENT_rodar})
ACAO_CLIENT_POR_TECLA.update({TECLA_direita:ACAO_CLIENT_rodar})
'''ACOES CLIENTE POR TECLA'''

