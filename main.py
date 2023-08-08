#Dicionario tem varios tipos de chaves e seus valores especificos de cada elemento;
#Ao colocar qualquer tipo de letra passa a ser uma string e deve ser acompanhada por aspas simples;
#Podemos colocar 2 elementos de uma um elemento podemos criar uma lista coom [];
tabela = {"alface":[0.45, 2009], "batata": 1.2, "tomate": 2.3, "feijão": 1.5}
print(tabela)

#Procura:
print(tabela["alface"])

#Modificar:
tabela["batata"] = "2.59"
print(tabela)

#Modificar com mais de um valor do elemento:
tabela["alface"] [1]= "Quantidade 5"
print(tabela)

#Deletar um elemento:
del tabela ["feijão"]
print(tabela)

#Adicionar elementos:
tabela["Manga"] = [5.68, "Quantidade 8"]
print(tabela)

#Pesquisar dentro do dicinario com boolean:
print("batata" in tabela)
print("berinjela in tabela")

#Imprime apenas as chaves:
print(tabela.keys())

#Imprime apenas os valores
print(tabela.values())

#Dicionarios - Interação com o usuario
while True:
    produtos = input("Digite o nome do produto que deseja procurar:")

    if produtos == "fim":
        break

    if produtos in tabela:
        print(f"Preço: R$ {tabela[produtos]:}")
    else:
        print("Produto não encontrado")

#Tuplas ->
