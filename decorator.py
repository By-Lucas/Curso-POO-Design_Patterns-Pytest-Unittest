'''
Decorator - é uma função que recebe outra função como parametro
gera uma nova função que adiciona algumas funcionalidades à função
original e a retorna essa nova função
'''

# EXEMPLO 1
def somar(a, b):
    return a + b

def modificar(funcao):
    def subtrair(a, b):
        return a - b
    return subtrair

@modificar
def somar(a, b):
    return a+b

#print(somar(2,3))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EXEMPLO 2

def modificar(funcao):
    def somar_pares(a, b):
        if a % 2 == 0 or b % 2 == 0:
            return a + b
        return a - b
    return somar_pares

@modificar
def somar(a, b):
    return a + b

#print(somar(3, 1))
#print(somar(3, 4))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EXEMPLO 3

def meu_decorador(funcao):
    def imprime_algo():
        print('Eu não sei de nada')
    return imprime_algo

@meu_decorador
def imprime():
    print('Eu sei de tudo')
    
imprime()