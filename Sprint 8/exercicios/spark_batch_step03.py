import random, os, time, names

random.seed (40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 50000 # limitei em 50k para ser possível subir para o github, uma vez que arquivos maiores de 100 megas são bloqueados

aux=[]
for i in range(0, qtd_nomes_unicos):
    aux.append(names.get_full_name())
print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))
dados= []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random. choice(aux))


file = open(f"./nomes_aleatorios.txt", "w")
for i in dados:
    file.write(f"{i}\n")
    