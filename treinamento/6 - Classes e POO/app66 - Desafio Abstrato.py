from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def AumentarClaridade(self, brilho):
        pass
    
    def ReduzirClaridade(self, brilho):
        pass

class MonitorFullHD(Monitor):
    def AumentarClaridade(self, brilho):
        print(f'Brilho aumentado para {brilho}')
    
    def ReduzirClaridade(self, brilho):
        print(f'Brilho diminuido para {brilho}')

monitor = MonitorFullHD()
monitor.AumentarClaridade(5)
monitor.ReduzirClaridade(5)