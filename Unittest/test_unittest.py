import unittest
import sys

"""
Se quiser mais detalhes da execução, pode executar da seguinte forma: python test_unittest.py -v
"""

class ConverterNumeroRomano:

    def __init__(self):
        self.digito_map = {"M": 1000, "D": 500, "C":100, "L": 50, "X": 10, "V": 5, "I": 1}
        
    def converter_para_decimal(self, numero_romano):
        val = 0
        for char in numero_romano:
            val += self.digito_map[char]
        return val


class TestConverterNumeroRomano(unittest.TestCase):

    def setUp(self):
        '''
        Executado antes de cada teste
        '''
        print('Construir o objeto da class ConverterNumeroRomano')
        self.cnr = ConverterNumeroRomano()

    def tearDown(self) -> None:
        '''
        Executado depois de cada teste
        '''
        print('Destruir o objeto da class ConverterNumeroRomano')
        self.cnr = None
    

    @unittest.skipIf(sys.version_info > (2,7), "Não suporta a versoes superiores a 2.7")
    def test_mil(self):
        #Pode ser utilizar o @unittest.skip para não executar esse teste ou,
        #@unittest.skipIf passando alguns parâmentros como pode ver acima
        self.assertEqual(1000, self.cnr.converter_para_decimal('M'))

    def test_cem(self):
        # Colocando o valor 1001 para forçar o erro
        self.assertEqual(100, self.cnr.converter_para_decimal('C'))

    def test_ciquenta(self):
        self.assertEqual(50, self.cnr.converter_para_decimal('L'))
    
    def test_vazio(self):
        self.assertTrue(self.cnr.converter_para_decimal('') == 0)
        self.assertFalse(self.cnr.converter_para_decimal('') > 0)


if __name__ == '__main__':
    unittest.main()