""" 
PERMITINDO APENAS A CRLAÇÃO DE UMA (1) INSTÂNCIA : SINGLETON
"""

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Test(metaclass=MetaSingleton):
    pass

t1 = Test()
t2 = Test()

print(t1, t2)