import sys

entrada = sys.stdin.readlines()

n = entrada[2]
n = n.split('n=')
qtde = int(n[1])


dados = []
for x in range(4, len(entrada)):
  dados.append((entrada[x]).split())

lista_adj = [[]for l in range(qtde)]
for i in range(len(dados)):
    vert1 = int(dados[i][0])
    vert2 = int(dados[i][1])
    lista_adj[vert1-1].append(vert2)
    lista_adj[vert2-1].append(vert1)

print(lista_adj)

