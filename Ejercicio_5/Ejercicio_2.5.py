from enum import Enum

class tipoCuenta(Enum):
  A = 'Ahorros'
  C = 'Corriente'

class cuentaBancaria:
  def __init__(self, nombresTitular, apellidosTitular, numCuenta, tipo: tipoCuenta):
    if not isinstance(tipo, tipoCuenta):
      raise ValueError("El tipo de cuenta debe ser 'tipoCuenta.A' o 'tipoCuenta.C'")
    self.nombresTitular = nombresTitular
    self.apellidosTitular = apellidosTitular
    self.numCuenta = numCuenta
    self.tipo = tipo.value
    self.saldo = 0

  def imprimirDatos(self):
    print("Nombres Titular: ", self.nombresTitular)
    print("Apellidos Titular: ", self.apellidosTitular)
    print("Numero de Cuenta: ", self.numCuenta)
    print("Tipo de Cuenta: ", self.tipo)
    print("Saldo: ", self.saldo, '\n')

  def consultarSaldo(self):
    return self.saldo

  def consignar(self, monto):
    if monto > 0:
      self.saldo += monto
      return True
    else:
      return False

  def retirar(self, monto):
    if self.saldo < monto:
      print('Saldo insuficiente\n')
      return False
    else:
      self.saldo -= monto
      return True


def main():
    cuenta = cuentaBancaria("Laura", "Martínez", "987654321", tipoCuenta.C)
    print("Datos iniciales:")
    cuenta.imprimirDatos()
    print(">> Consulta de saldo:")
    print("Saldo actual:", cuenta.consultarSaldo(), '\n')
    print(">> Consignación de $200000:")
    cuenta.consignar(200000)
    print("Saldo después de consignar:", cuenta.consultarSaldo(), '\n')
    print(">> Retiro de $50000:")
    cuenta.retirar(50000)
    print("Saldo después del retiro:", cuenta.consultarSaldo(), '\n')
    print(">> Intento de retiro de $300000 (más de lo disponible):")
    cuenta.retirar(300000)
    print("Saldo final:", cuenta.consultarSaldo())

if __name__ == "__main__":
    main()
