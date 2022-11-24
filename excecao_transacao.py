

class TransacaoInvalida(Exception):
    def __init__(self, saldo_atual, quantidade) -> None:
        super().__init__('Sua conta nao tem R$ {}'. format(quantidade))

        self.saldo_atual = saldo_atual
        self.quantidade = quantidade

    def excesso(self):
        return self.quantidade - self.saldo_atual

try:
    raise TransacaoInvalida(10, 50)
except TransacaoInvalida as e:
    print('Voce nao tem saldo suficiente, falta R$ {}'.format(e.excesso()))