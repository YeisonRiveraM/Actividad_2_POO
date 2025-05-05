from enum import Enum

class tipoCombustible(Enum):
  GASOLINA = "Gasolina"
  BIOETANOL = "Bioetanol"
  DIESEL = "Diesel"
  BIODIESEL = "Biodiesel"
  GAS_NATURAL = "Gas Natural"

class tipoAutomovil(Enum):
  CIUDAD = "Ciudad"
  SUBCOMPACTO = "Subcompacto"
  COMPACTO = "Compacto"
  FAMILIAR = "Familiar"
  EJECUTIVO = "Ejecutivo"
  SUV = "SUV"

class tipoColor(Enum):
  BLANCO = "Blanco"
  NEGRO = "Negro"
  ROJO = "Rojo"
  NARANJA = "Naranja"
  AMARILLO = "Amarillo"
  VERDE = "Verde"
  AZUL = "Azul"
  VIOLETA = "Violeta"

class automovil:
  def __init__(self, marca, modelo, motor, tipoCombustible, tipoAutomovil, numeroPuertas, cantidadAsientos, velocidadMaxima, color):
    self.marca = marca
    self.modelo = modelo
    self.motor = motor
    self.tipoCombustible = tipoCombustible
    self.tipoAutomovil = tipoAutomovil
    self.numeroPuertas = numeroPuertas
    self.cantidadAsientos = cantidadAsientos
    self.velocidadMaxima = velocidadMaxima
    self.color = color
    self.velocidadActual = 0

  def get_marca(self):
    return self.marca

  def get_modelo(self):
    return self.modelo

  def get_motor(self):
    return self.motor

  def get_tipoCombustible(self):
    return self.tipoCombustible

  def get_tipoAutomovil(self):
    return self.tipoAutomovil

  def get_numeroPuertas(self):
    return self.numeroPuertas

  def get_cantidadAsientos(self):
    return self.cantidadAsientos

  def get_velocidadMaxima(self):
    return self.velocidadMaxima

  def get_color(self):
    return self.color

  def get_velocidadActual(self):
    return self.velocidadActual

  def set_marca(self, marca):
    self.marca = marca

  def set_modelo(self, modelo):
    self.modelo = modelo

  def set_motor(self, motor):
    self.motor = motor

  def set_tipoCombustible(self, tipoCombustible):
    self.tipoCombustible = tipoCombustible

  def set_tipoAutomovil(self, tipoAutomovil):
    self.tipoAutomovil = tipoAutomovil

  def set_numeroPuertas(self, numeroPuertas):
    self.numeroPuertas = numeroPuertas

  def set_cantidadAsientos(self, cantidadAsientos):
    self.cantidadAsientos = cantidadAsientos

  def set_velocidadMaxima(self, velocidadMaxima):
    self.velocidadMaxima = velocidadMaxima

  def set_color(self, color):
    self.color = color

  def set_velocidadActual(self, velocidadActual):
    self.velocidadActual = velocidadActual

  def acelerar(self, incremento):
    if (self.velocidadActual + incremento) < self.velocidadMaxima:
      self.velocidadActual += incremento
    else:
      print("No se puede incrementar a una velocidad superior a la máxima del automóvil.")

  def desacelerar(self, decremento):
    if (self.velocidadActual - decremento) > 0:
      self.velocidadActual -= decremento
    else:
      print("No se puede decrementar a una velocidad negativa.")

  def frenar(self):
    self.velocidadActual = 0

  def tiempoLlegada(self, distancia):
    return distancia / self.velocidadActual

  def imprimir(self):
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Motor: {self.motor}")
    print(f"Tipo de Combustible: {self.tipoCombustible.value}")
    print(f"Tipo de Automóvil: {self.tipoAutomovil.value}")
    print(f"Número de Puertas: {self.numeroPuertas}")
    print(f"Cantidad de Asientos: {self.cantidadAsientos}")
    print(f"Velocidad Máxima: {self.velocidadMaxima} km/h")
    print(f"Color: {self.color.value}")
    

def main():
  auto1 = automovil("Ford", 2018, 3, tipoCombustible.DIESEL, tipoAutomovil.EJECUTIVO, 5, 6, 250, tipoColor.NEGRO)
  auto1.imprimir()
  auto1.set_velocidadActual(100)
  print(f"Velocidad actual: {auto1.velocidadActual} km/h")
  auto1.acelerar(20)
  print(f"Velocidad actual: {auto1.velocidadActual} km/h")
  auto1.desacelerar(50)
  print(f"Velocidad actual: {auto1.velocidadActual} km/h")
  auto1.frenar()
  print(f"Velocidad actual: {auto1.velocidadActual} km/h")
  auto1.desacelerar(20)

if __name__ == "__main__":
    main()