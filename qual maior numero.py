numero = None
print(f"antes {numero}")
for conjunto in [-99,-1, 41, 4, 74, 12, 15]:
    if numero is None:
        numero = conjunto
    elif numero < conjunto:
        numero = conjunto
    print(numero, conjunto)
print(f"portanto, {numero} é o maior número do conjunto")
