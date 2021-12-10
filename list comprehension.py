def comprehension(lista_iteravel):
    lista = [value for indice, valor in enumerate(lista_iteravel) if indice % 2 == 0]
    return lista
    
print(comprehension(["a", "b", "c", "d", "e", "f", "g"])) 

# deve ter uma saída como: ['a', 'c', 'e', 'g']
