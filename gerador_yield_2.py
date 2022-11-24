

def is_prime(number):
    for i in range(3, number):
        if number % i == 0:
            return False
    return True

# def get_primos(input_list):
#     return (e for e in input_list if is_prime(e))

def gerar_numeros():
    yield 1
    yield 2
    yield 3

'''
for v in gerar_numeros():
    print(v, end= ' ')
'''
# A função que retorna yield, ela é geradora, e por ser usada num loop for...
# Quando utilizada o next, ela salva a seção, e executa a proxima: Exemplo: -->
#  se ela for chamada uma vez, ela vai ser executada na proxima, se usar o next
'''
nosso_gerador = gerar_numeros()
print(next(nosso_gerador))
print(next(nosso_gerador))
print(next(nosso_gerador))
'''

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

meu_gerador = get_primes(10)
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))