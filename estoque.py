estoque = {"Folhas de Sulfite": [500,50.99], "Canetas Bic":[300, 2.50], "Cadernos":[50, 70.99], "Régua":[15,6.84], "Lapis":[30,0.60]}

venda = [["Folhas de Sulfite",5],["Lapis",10]]

total = 0

for op in venda:
    produto, quantidade = op
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto}:{quantidade} X {preco} = {custo}")
    estoque[produto][0] -= quantidade
    total += custo
print(f"(Custo Total:{total}")

for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print(f"Preço: R$ {dados[1]}")


