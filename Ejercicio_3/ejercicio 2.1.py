class Persona:
    def __init__(self, nombre, apellidos, numero_documento_identidad, anio_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento_identidad = numero_documento_identidad
        self.anio_nacimiento = anio_nacimiento
    def imprimir(self):
        """Imprime los datos de la persona"""
        print("Nombre =", self.nombre)
        print("Apellidos =", self.apellidos)
        print("Número de documento de identidad =", self.numero_documento_identidad)
        print("Año de nacimiento =", self.anio_nacimiento)
        print()
if __name__ == "__main__":
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    p2 = Persona("Luis", "León", "1053223344", 2001)
    p1.imprimir()
    p2.imprimir()