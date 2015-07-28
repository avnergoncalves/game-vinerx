'''
Created on 16/01/2012

@author: avner.goncalves
'''
import re

def v_encode(lista):        
    lista = ' ;'.join(lista)
    
    return lista

def v_decode(string):
    string = re.split('[^:];', string)  
    
    r = []    
    for i in string:
        i = str(i).replace(':;', ';')
        r.append(i)
        
    return r