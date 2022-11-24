import math

class Forma():

    def __init__(self) -> None:
        print('Construtor da forma')

    def area(self):
        print('Area da forma')
    
    def perimetro(self):
        print(f'Perimetro da forma')

    def descricao(self):
        print('Descricao da forma')


class Quadrado(Forma):
    """
    Herdando a a Super Classe:
    Se criar funcoes e variaveis iguais a da Super classe,
    ela será reescrevida pela Sub Classe
    """
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4


class Circulo(Forma):
    """
    Herdando a a Super Classe:
    Se criar funcoes e variaveis iguais a da Super classe,
    ela será reescrevida pela Sub Classe
    """
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def descricao(self):
        print('Descricao do circulo')


# VALORES DA CLASSE QUADRADO
quad = Quadrado(2)
print('Area quadrado: %d' % quad.area())
print('Perimetro quadrado: %d' %quad.perimetro())
quad.descricao()
""" Como nao foi criada um metodo descricao, ele nao sofre alteracoes"""


# VALORES DA CLASSE CIRCULO
circulo = Circulo(3)
print('Area circulo: %f' % circulo.area())
print('Perimetro circulo: %f' % circulo.perimetro())
circulo.descricao()