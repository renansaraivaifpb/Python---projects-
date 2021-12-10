def informacao(pessoa):
  for indice, valor in enumerate(pessoa):
    print('{} tem {} anos e trabalha como {}'.format(valor[0], valor[1], valor[2]))

informacao([('Ken', 30, "Cozinheira"), ("Pat", 35, 'Advogada'), ('Amanda', 25, "Engenheira de Controle e Automação")])



''' saída: 
Ken tem 30 anos e trabalha como Cozinheiro
Pat tem 35 anos e trabalha como Advogada
Amanada tem 25 anos e trabalha como Engenheira de Controle e Automação
'''
