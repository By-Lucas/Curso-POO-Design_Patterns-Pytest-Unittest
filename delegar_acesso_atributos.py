
class A:

    def fazer_algo(self):
        pass

    def alguma_coisa(self):
        pass

    def algum_metodo(self, nome):
        return nome

class B:

    def __init__(self) -> None:
        self.a = A()

    
    def fazer_algo(self):
        return self.a.fazer_algo()

    def alguma_coisa(self):
        return self.a.alguma_coisa()

    def __getattr__(self, nome):
        return getattr(self.a, nome)

b = B()
b.fazer_algo() # Chama o B.fazer_algo() (existe na classe B)

"""Quando não achar o metodo na classe B, ele vasculha na classe A"""
print(b.algum_metodo('Python')) # Chama o B.__getattr__('algum_metodo) e delega para a.algum_metodo()
