
# Programa escrito em python que calcula automaticamente (em função) pagamentos x taxa por hora, menor que 40 horas, um pagamento normal, um pagamento superior a 40 horas, cobre 1.5*taxa das horas trabalhas acima de 40h somado com as 40h trabalhadas
horas = float(input("Digite horas: "))
taxas = float(input("Digite taxa por hora: "))
def calcularpagamento (horas, taxas):
   if horas > 40:
       pagamento = 1.5 * taxas * (horas - 40) + (40 * taxas)
       return pagamento
   else:
        # O pagamento deve ser o valor normal para horas de até 40 horas 
        pagamento = horas * taxas
        return pagamento 
print(f"Pagamento: {calcularpagamento(horas, taxas)}")

