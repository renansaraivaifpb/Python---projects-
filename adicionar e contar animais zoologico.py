class Zoo:
    def __init__(self):
        self.banco_dados = {}
    def adicionar_animal(self, nome, categoria):
        self.banco_dados[nome] = categoria
    def contar_animais(self, categoria):
        '''contar quantos animais está contido em um conjunto(categoria) x'''
        contagem = 0
        for animal in self.banco_dados.values():
            if animal in categoria:
                contagem += 1
        return contagem
zoo = Zoo()

class Animal:
    nome = ''
    categoria = ''
    def __init__(self,nome):
        self.nome = nome
        self.categoria = self.categoria
class Macacos(Animal):
    categoria = 'mamiferos'
class Reptios(Animal):
    categoria = 'réptios'


jarde = Macacos('jarde')
zoo.adicionar_animal(jarde.nome, jarde.categoria)
cobra = Reptios('cobra_noite')
zoo.adicionar_animal(cobra.nome, cobra.categoria)
cobra = Reptios('cobra_dia')
zoo.adicionar_animal(cobra.nome, cobra.categoria)


print(zoo.banco_dados)
print(zoo.contar_animais(cobra.categoria))
