'''
Created on 26/09/2012

@author: avner.goncalves
'''

class ReenviaPacotes(object):
    '''    
    '''        
        
    def executar(self):
        '''        
        '''                    
        pkts_perdidos = vinerOnline.get_pacotes_perdidos()
        
        if len(pkts_perdidos) > 0:
            for pkt in pkts_perdidos:
                endereco = pkt.get_endereco()
                tipo     = pkt.get_tipo()
                acao     = pkt.get_acao()
                args     = pkt.get_args()
                
                vinerOnline.envia_pacote(endereco, tipo, acao, args)            
            