import nose

"""
pip install nose
Com essa biblioteca você pode estar fazendo os testes do pytest e Unittest, e configurando-os 
da maneira que desejar na hora da execução
"""

# Executando de maneira verbosa(detalhada)
config = nose.config.Config(verbosity=10) #quantidade (verbosity=10)

nose.run(config=config)