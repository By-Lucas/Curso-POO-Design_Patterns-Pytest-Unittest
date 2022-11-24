
"""
É BOM UTILIZAR O Except BaseExcept em vez de except Exception, porque o Exception
erda de BaseExcept e tem outros erros que só tem na classe mãe BaseExcept
"""

class SomentePares(list):

    def append(self, inteiro):
        if not isinstance(inteiro, int):
            raise TypeError("Somente inteiros")
        if inteiro % 2:
            raise ValueError("Somente pares")

        super().append(inteiro)

sp = SomentePares()
sp.append(4)