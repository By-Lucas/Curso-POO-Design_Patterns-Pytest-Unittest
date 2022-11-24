import json


class Contato:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return ('{} {}'. format(self.nome, self.sobrenome))


c = Contato('Lucas', 'Silva')
print(json.dumps(c.__dict__))
        