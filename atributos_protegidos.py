
class P:
    def __init__(self, x) -> None:
        """
        Um atribulo com 1 Underline (_x) na frente
        é um atribulo privado (pode ser classes e metodos), e tem um motivo de ele estar assim
        pode ser importante e geralmente só pode ser acessado dentro da classes.
        """
         # Atribulo privado, mas o interpretador python entende como publico
        self._x = 5

        """
        Um atribulo com 2 Undeline (__x) se refere a um atribulo protegido,
        não pode ser acessado fora da classes, somente dentro da classes.
        Para que não haja alterações nele a classes o esconde e muda o nome, mas é possivel acessa-lo
        """
        self.__x = x

obj = P(10)
print(obj._x) # Atribulo privado, mas o interpletador entende como publico
print(obj._P__x) # Atributo protegido