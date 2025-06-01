import random
import math
from typing import List, Tuple

class Coordenada:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distancia_origen(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        return f"[{self.x}, {self.y}]"

def generar_coordenadas(n: int) -> List[Coordenada]:
    return [Coordenada(random.randint(-81, 81), random.randint(-81, 81)) for _ in range(n)]

def encontrar_mas_alejada(coordenadas: List[Coordenada]) -> Coordenada:
    if not coordenadas:
        return None
    if len(coordenadas) == 1:
        c = coordenadas[0]
        if c.x > 0 and c.y < 0:
            return c
        else:
            return None

    mitad = len(coordenadas) // 2
    izquierda = encontrar_mas_alejada(coordenadas[:mitad])
    derecha = encontrar_mas_alejada(coordenadas[mitad:])

    if izquierda and derecha:
        return izquierda if izquierda.distancia_origen() > derecha.distancia_origen() else derecha
    return izquierda or derecha

def main():
    n = int(input("Ingrese la cantidad de pares de coordenadas: "))
    matriz = generar_coordenadas(n)

    print("\nCoordenadas generadas:")
    for c in matriz:
        print(c)

    resultado = encontrar_mas_alejada(matriz)
    
    if resultado:
        print(f"\nCoordenada más alejada con X > 0 e Y < 0: {resultado}")
        print(f"Distancia desde el origen: {resultado.distancia_origen():.2f}")
    else:
        print("\nNo se encontraron coordenadas con X > 0 e Y < 0.")

if __name__ == "__main__":
    main()
