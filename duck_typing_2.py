

class Pato:

    def quack(self):
        print('Quack, quack')
    

class Pessoa:

    def quack(self):
        print('Eu faço quack igual a um pato')


# Isso NÃO é Pythonico
"""
def fazer_quack(obj):

    # Se obj for uma instancia de Pato
    if isinstance(obj, Pato):
        obj.quack()
    else:
        print('Isso tem que ser um pato')
"""

"""
def fazer_quack(obj):
    # LBYL #= ESTICO DE CODIFICAÇÃO "NÃO PYTHONICO"

    # Verifica se tem um atributo
    if hasattr(obj, 'quack'):
        # se for chamavel
        if callable(obj.quack):
            obj.quack()
"""

# RECOMENDADO
def fazer_quack(obj):
    # EAFP = CODIFICAÇÃO PYTHONICO E MAIS SIMPLES
    try:
        obj.quack()
    except AttributeError as e:
        print(e)


pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)