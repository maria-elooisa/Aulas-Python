#tuplas, não é permitido alterar os valores

comida = ("Lasanha", "Feijoada", "Sushi")
print(comida)

cmd1, cmd2, cmd3 = comida
print(cmd1)
print(cmd2)
print(cmd3)

#Desempacotamento, criando variaveis aos valores.
comidas1 =("Panqueca",)
print(type(comidas1))

comidas2 = ("Fritas",)
print(type(comidas2))

comidas3 = comidas1 + comidas2 + comida
print(comidas3)
print(len(comidas3)) #Retorna a quantidade de valores




