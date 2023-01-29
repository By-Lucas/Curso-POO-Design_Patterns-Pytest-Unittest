class Funcionario:

    def __init__(self, nome, salario, cpf):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf

    def get_bonificacao(self):
        return self.salario * 0.20

class Gerente(Funcionario):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.senha = senha
    
    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.00

g = Gerente('Lucas', 3000.00, '1111111111', '123')

print('Nome:', g.nome)
print('Salário:', g.salario)
print('Salário com Bonificação:', g.get_bonificacao())
print('CPF:', g.cpf)
print('Senha:', g.senha)
