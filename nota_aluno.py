#faça um programa em python que o usuário insirá duas notas e calcule se ele passou ou não
#EDIT (24/11/2021): palavra reservada do python try e except permite verificar se as notas são realmente possiveís de convertelas para tipo float, caso contrário, possivelmente, 
não foi inserido numeros no input que tem como tipo string, logo, o except fecha o programa. 
nota_1 = input('Digite sua primeira nota: ')
nota_2 = input('Digite sua segunda nota: ')
try:
    verificar_nota1 = float(nota_1)
    verificar_nota2 = float(nota_2)
except:
    print("Há um erro nas entradas de nota, possivelmente: não numérico. Tente novamente.")
    quit()
media = (nota_1 + nota_2) / 2
if media >= 7:
    print(f"Sua média é {media}. Logo, você está APROVADO!")
elif media < 7:
    print(f"Sua média é {media}. Portanto, você está REPROVADO!")
