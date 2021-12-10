def iterar(lista_iterativa):
  nova_lista = []
  i = 0
  for i in range(0, len(lista_iterativa),2):
    nova_lista.insert(i, lista_iterativa[i])
  return nova_lista
#remove elemento 2, 4, 6

print(iterar(["a", "b", "c", "d", "e", "f", "g"])) 
# Deve sair: ['a', 'c', 'e', 'g'] 
# isto oé, valores destes índices: [0, 2, 4,6]
