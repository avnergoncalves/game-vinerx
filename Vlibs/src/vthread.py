# To change this template, choose Tools | Templates
# and open the template in the editor.

#from direct.stdpy import threading
import threading

count_thread = 0

class ThreadControle(threading.Thread):
    def __init__(self, count, delay, funcao, nome, *args):
        threading.Thread.__init__(self)
        
        self.__count    = count
        self.__delay    = delay
        self.name       = nome
        self.__funcao   = funcao
        self.__args     = args
        self.__finished = threading.Event()
        
    def get_count(self):
        return self.__count
    
    def get_delay(self):
        return self.__delay
    
    def get_funcao(self):
        return self.__funcao    
     
    def set_delay(self, delay):
        self.__delay = delay
    
    def run(self):
        global count_thread
        try:
            count_thread += 1

            if self.__count == 0:
                ct = -1
            else:
                ct = 0

            while ct < self.__count and not self.__finished.isSet():
                if len(self.__args) > 0:
                    self.__funcao(*self.__args)
                else:
                    self.__funcao()
                    
                if ct == -1:
                    ct = -1
                else :
                    ct += 1

                self.__finished.wait(self.__delay)
        finally:
            del self.__funcao, self.__args
            count_thread -= 1

    def stop_thread(self, delay = 0):
        self.__finished.wait(delay)
        self.__finished.set()
        #self.join()

class vThread(object):

    def __init__(self):
        self.allThread      = {}
        self.__esta_rodando = False

    def add(self, count, delay, funcao, nome, *args):
        if self.allThread.has_key(nome):
            self.parar(nome)
            del self.allThread[nome]

        self.allThread[nome] = ThreadControle(count, delay, funcao, nome, *args)
        
        if self.__esta_rodando:
            self.allThread[nome].start()

    def get(self, nome = False):
        if nome:
            return self.allThread[nome]
        else:
            return self.allThread

    def parar(self, nome = False, delay = 0):
        if nome:
            if isinstance(nome, dict):
                for i in nome:
                    self.allThread[i].stop_thread(delay)
            else:
                self.allThread[nome].stop_thread(delay)
        else:
            for i in self.allThread:                
                self.allThread[i].stop_thread(delay)
        
            self.__esta_rodando = False

    def iniciar(self, nome = False):
        if nome:
            if isinstance(nome, dict):
                for i in nome:
                    if not self.allThread[i].isAlive():
                        self.allThread[i].start()
            else:
                if not self.allThread[nome].isAlive():
                    self.allThread[nome].start()
        else:
            for i in self.allThread:                
                if not self.allThread[i].isAlive():
                    self.allThread[i].start()
        
        self.__esta_rodando = True
    
def inicia_nova_thread(count, delay, funcao, nome, *args):
    thr = ThreadControle(count, delay, funcao, nome, *args)
    thr.start()
    return thr

def get_count_thread():
    global count_thread
    return count_thread