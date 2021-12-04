
def somar_areas_triangulos (comprimento, altura):
  return (comprimento*altura)/2
for i in [1, 2, 3, 4]:
  area_total = 0
  c = float(input("Digite comprimento (m): ")
  a = float(input("Digite altura (m): ")
  triangulo = somar_areas_triangulos (c,a)
  print(f"A área do triangulo {i} é: {triangulo} m²")
  area_total = area_total + triangulo
print(f"A soma das áreas dos quatros triângulos é: {area_total} m²")
