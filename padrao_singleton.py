'''
Padrão de projeto Singleton

1 - Oferecer 1 ponto de acesso a um objeto que seja de uso global,
2 - Controlar o processo concorrente a recursos compartilhados,
3 - Garantir que só pode ser criado um objeto da classe seja criado
'''

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            # hasattr = Para saber se um objeto tem a propriedade instance
            # Se o objeto existir, ele vai retornar o mesmo valor do objeto existente
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
print(s1)
s2 = Singleton()
print(s2)