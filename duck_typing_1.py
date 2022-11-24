"""
Duck Typing é utilizado quando um método de uma função tem
praticamente as mesmas funcionalidades, e pode ser utilizdada 
num mesmo método.

Programe para interfaces e não para um implementação
"""

class Pato:
    def quack(self):
        print('Pato quack quack')


class Pessoa:
    def quack(self):
        print('Pessoa QUACK!')


def na_floresta(obj):
    obj.quack()

na_floresta(Pato())
na_floresta(Pessoa())