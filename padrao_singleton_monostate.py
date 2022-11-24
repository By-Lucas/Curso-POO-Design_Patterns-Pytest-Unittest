"""CRIAM VARIOS OBJETOS COM INSTANCIAS QUE COMPARTILHAM OS MESMOS ESTADOS"""

class MinhaClasse:
    __estado_compatilhado = {'1': 2}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__estado_compatilhado


# OBJETOs
b1 = MinhaClasse()
b2 = MinhaClasse()

b1.x = 5

# OBJETOS DIFERENTES (DISTINTOS)
print('b: ', b1)
print('b: ', b2)

# COMPARTILHAM OS MESMOS ESTADOS
print(b1.__dict__)
print(b2.__dict__)
