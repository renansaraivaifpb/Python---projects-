#faça um programa em python que o usuário insirá duas notas e calcule se ele passou ou não
nota_1 = int(input('Digite sua primeira nota: '))
nota_2 = int(input('Digite sua segunda nota: '))
media = (nota_1 + nota_2) / 2
if media >= 7:
    print(f"Sua média é {media}. Logo, você está APROVADO!")
elif media < 7:
    print(f"Sua média é {media}. Portanto, você está REPROVADO!")