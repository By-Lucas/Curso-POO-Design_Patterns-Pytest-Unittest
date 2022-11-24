from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def som(self):
        pass


class Cachorro(Animal):
    def som(self):
        print('au au au')


class Gato(Animal):
    def som(self):
        print('miau miau miau')


class Fabrica(object):
    def reproduzir_som(self, object_type):
        return eval(object_type)().som()


if __name__ == "__main__":
    """
    Passando a classe como String dentro do método
    """
    f = Fabrica()
    f.reproduzir_som('Gato')