
class Data:
    
    def __init__(self, dia, mes, ano) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)
        
    @classmethod
    def de_string(cls, data_string): #10-10-2022 data no formato string
        """
        Metodo de classe recebe a classse como primeiro argumento
        Pode-se criar novas instancias atraves do cls, pode ser erdada e resinscrita
        """
        mes, dia, ano = map(int, data_string.split('-'))
        data = cls(mes, dia, ano) # Chama a classe novamente, mas num formato de variavel
        return data

    @staticmethod
    def is_date_valid(data_string):
        """
         @staticmethod = Não tem referencia com objeto e nem com a classe
         nao se pode erdar e nao altera-la(uma funcao dentro da classes) e nem substituir
        """
        mes, dia, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 2022





cl = Data(10, 10, 10)
data1 = Data.de_string("10-10-2022")
print(data1)
print(data1.is_date_valid("10-10-2022"))