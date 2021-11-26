valor_menor = None
for corredores in [9, 4, 48, 2, 15, 72, 7]:
    if valor_menor is None: # is None (-50%) more fast than "== None"
        valor_menor = corredores
        print(f"este é o primeiro número do conjunto {valor_menor}")
    elif corredores < valor_menor:
        valor_menor = corredores
    print(f"corredor {corredores} | menor numero {valor_menor}")
print(f"concluimos que {valor_menor} é o menor numero do conjunto.")
