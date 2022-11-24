
class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    @classmethod
    def outro_contrutor(cls, nome): #Recebe a classe como primero argumento
        return cls(nome)

"""
p = Pessoa('Lucas')
print(p.nome)
"""
p = Pessoa.outro_contrutor('Pedro')
print(p.nome)