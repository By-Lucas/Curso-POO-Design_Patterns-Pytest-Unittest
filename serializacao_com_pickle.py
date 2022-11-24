import pickle

# EXEMPLO DE SERIALIZAÇÃO DE OBJETOS COM PICKLE
meus_dados = ['lucas', 3.14, [1, 2, 3, 4]]

# Criando arquivo.txt e salvando meus_dados dentro dele
with open('arquivo.txt', 'wb') as file:
    pickle.dump(meus_dados, file)

# Carregado os dados salvo no arquivo.txt
with open('arquivo.txt', 'rb') as file:
    dados_carregados = pickle.load(file)

print(meus_dados)
