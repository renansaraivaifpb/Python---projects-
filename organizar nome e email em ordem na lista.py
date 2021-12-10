def dados(informacoes):
    lista = []
    for email, nome in informacoes:
        lista.append(f"Nome: {nome} | E-mail: <{email}>")
    return lista
print(dados([('renan@example.com', 'Renan'),('saraiva@example.com', 'Saraiva')]))

''' saída:
[Nome: Renan | E-mail: <renan@example.com>
[Nome: Saraiva | E-mail: <saraivan@example.com>
'''
