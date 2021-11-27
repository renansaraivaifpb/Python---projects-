maior_numero = None
menor_numero = None
while True:
    digitado = input("Digite: ")
    try:
    	digitado = int(digitado)
    except:
        if digitado == "done":
        	break
        else:
        	print("Invalid input")
        continue
    if maior_numero is None and menor_numero is None:
        maior_numero = digitado
        menor_numero = digitado
    elif maior_numero < digitado:
    	maior_numero = digitado
print(f"Maximum is {maior_numero}\nMinimum is {menor_numero}")
