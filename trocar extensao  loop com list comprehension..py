arquivos = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Gere novos nomes de arquivos como uma lista contendo os novos nomes de arquivos 
# usando quantas linhas de código forem necessárias para o método escolhido.
novos arquivos = [valor.replace('.hpp','.h') for indice, valor in enumerate(arquivos)] 
print(novos arquivos) 
# Deve ser> ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
