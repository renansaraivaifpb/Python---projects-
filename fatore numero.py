def fatorial(n):
    resultado = 1
    for contador in range(1,n+1):
        resultado = resultado * contador
    return resultado
numero = int(input("Digite um número para saber seu resultado em fatorial: "))
print(fatorial(numero))
