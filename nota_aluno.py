#faça um programa em python que o usuário insirá duas notas e calcule se ele passou ou não
nota_1 = input('Digite sua primeira nota: ')
nota_2 = input('Digite sua segunda nota: ')
try:
    verificado_nota1 = float(nota_1)
    verificado_nota2 = float(nota_2)
except:
    print("Há um erro nas entradas de nota, possivelmente: não numérico. Tente novamente.")
    quit()
media = (verificado_nota1 + verificado_nota2) / 2
if media >= 7:
    print(f"Sua média é {media}. Logo, você está APROVADO!")
elif media < 7:
    print(f"Sua média é {media}. Portanto, você está REPROVADO!")
