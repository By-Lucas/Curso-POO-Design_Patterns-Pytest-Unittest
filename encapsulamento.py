# Encapsulamento
# Encapsulamento é a técnica que faz com que os detalhes internos do funcionamento 
# dos métodos de uma classe fiquem ocultos para os objetos.

""" 
Não altera o valor do atributo inicial, então se tiver
outros programas utilizando a variavel , ele não interrompe nenhuma outra atividade
ele apenas vai modificar para o seu uso em determinada aplicação, e não no modo geral
"""

class P():

    def __init__(self, x):
        self.x = x
    
    @property 
    def x(self):
        # pegar a variavel(como se fosse um request.get na variavel)
        return self._x
    
    @x.setter # Setando outro valor na variavel(encapsulando)
    def x(self, x):
        if x > 0:
            self._x = x

p = P(10)
print(p.x)
p.x = 5
print(p.x)