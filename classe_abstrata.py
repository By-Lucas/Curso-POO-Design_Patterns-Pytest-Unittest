from abc import ABCMeta, abstractmethod

"""
Metodo abstrato não possui implementação e não pode ser instanciada diretamente,
somente atraves das sublasses
"""

# MinhaClasseAbstrata é uma instancia de metaclass=ABCMeta
class Animal(metaclass=ABCMeta):

    @abstractmethod
    def dizer_algo(self):
        return "Eu sou um animal"


class Cachorro(Animal):

    def latir(self):
        return "LATINDO"

    def dizer_algo(self):
        # Dessa forma pode-se ter acesso aos métodos abstratos 
        # dentro da super classe
        s = super(Cachorro, self).dizer_algo()
        return "%s - %s" % (s, 'AU AU')

a = Cachorro()
print(a.dizer_algo())