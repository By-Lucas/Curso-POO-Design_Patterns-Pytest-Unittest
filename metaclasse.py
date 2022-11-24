"""
METACLASSE = É uma classe de outra classe (ela é uma instância de sua metaclasse)
"""

class MetaClasse(type):
    def __call__(cls, *args, **kwargs) :
        print('Minha metaclasse', args)
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MetaClasse):
    def __init__(self, x, y) :
        self.x = x
        self.x = y

obj = int(4, 5)
        