import math
class circulo:
  def __init__(self, radio):
    self.radio = radio
  def calcArea(self):
    return math.pi * self.radio ** 2
  def calcPerimetro(self):
    return 2 * math.pi * self.radio

class rectangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  def calcArea(self):
    return self.base * self.altura
  def calcPerimetro(self):
    return (2*self.base) + (2*self.altura)
  
class cuadrado:
  def __init__(self, lado):
    self.lado = lado
  def calcArea(self):
    return self.lado**2
  def calcPerimetro(self):
    return self.lado*4

class trianguloRect:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
  def calcArea(self):
    return (self.base * self.altura)/2
  def calcPerimetro(self):
    return self.base + self.altura + self.calcHipotenusa()
  def calcHipotenusa(self):
    return ((self.base**2) + (self.altura**2))**(0.5)
  def tipoTriangulo(self):
    if self.base==self.altura==self.calcHipotenusa():
      print("Es un triángulo equilátero")
    elif (self.base != self.altura) and (self.base != self.calcHipotenusa) and (self.altura != self.calcHipotenusa):
      print("Es un triángulo escaleno")
    else:
      print("Es un triángulo isósceles")

def main():
  fig1 = circulo(2)
  fig2 = rectangulo(1, 2)
  fig3 = cuadrado(3)
  fig4 = trianguloRect(3, 5)

  print(f"El área del círculo es: {fig1.calcArea()}")
  print(f"El perímetro del cículo es: {fig1.calcPerimetro()}\n")
  print(f"El área del rectángulo es: {fig2.calcArea()}")
  print(f"El perímetro del rectángulo es: {fig2.calcPerimetro()}\n")
  print(f"El área del cuadrado es: {fig3.calcArea()}")
  print(f"El perímetro del cuadrado es: {fig3.calcPerimetro()}\n")
  print(f"El área del triángulo es: {fig4.calcArea()}")
  print(f"El perímetro del triángulo es: {fig4.calcPerimetro()}")
  fig4.tipoTriangulo()

if __name__ == "__main__":
    main()
