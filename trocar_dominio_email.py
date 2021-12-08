# função trocar_dominio(email_completo, novo_dominio) captura os argumentos digitados e troca o dominio antigo para o dominio novo que deseja (digitado).

def trocar_dominios(email_completo, novo_dominio):
  index = email_completo.index('@')
  novo_email = email_completo[:index] + "@" + novo_dominio
  print(f"O seu novo e-mail agora é: novo_email")
email_digitado = input("Digite o seu e-mail: ")
novo_dominio_digitado = input("Digite o seu novo domínio: ")
trocar_dominios(email_digitado, novo_dominio_digitado)
