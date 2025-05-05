from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:
    def __init__(self, nombre: str, cantidad_satelites: int, masa: float, volumen: float,
                 diametro: int, distancia_sol: int, tipo: TipoPlaneta, es_observable: bool):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self) -> float:
        return self.masa / self.volumen

    def es_planeta_exterior(self) -> bool:
        limite = 149_597_870 * 3.4
        return self.distancia_sol > limite

if __name__ == "__main__":
    p1 = Planeta(
        "Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150_000_000, TipoPlaneta.TERRESTRE, True
    )
    p1.imprimir()
    print(f"Densidad del planeta = {p1.calcular_densidad()}")
    print(f"Es planeta exterior = {p1.es_planeta_exterior()}\n")

    p2 = Planeta(
        "Júpiter", 79, 1.899E27, 1.4313E15, 139820, 750_000_000, TipoPlaneta.GASEOSO, True
    )
    p2.imprimir()
    print(f"Densidad del planeta = {p2.calcular_densidad()}")
    print(f"Es planeta exterior = {p2.es_planeta_exterior()}")