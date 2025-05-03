import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

equipo1 = Equipo("Alianza Lima")
equipo2 = Equipo("Universitario")

def RegistraSet(equipoGanador):
    global equipo1, equipo2
    if equipoGanador == 1:
        equipo1.setGanados += 1
    elif equipoGanador == 2:
        equipo2.setGanados += 1

    if equipo1.setGanados == 3:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
        print(f"Partido para {equipo1.nombre}")
        equipo1.setGanados = 0
        equipo2.setGanados = 0
        return True  
    elif equipo2.setGanados == 3:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1
        print(f"Partido para {equipo2.nombre}")
        equipo1.setGanados = 0
        equipo2.setGanados = 0
        return True  
    return False  

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    partido_terminado = False
    while not partido_terminado:
        puntos1 = Puntos()
        puntos2 = Puntos()
        
        while puntos1 < 25 and puntos2 < 25:
            puntos1 += PuntosExtras()
            puntos2 += PuntosExtras()
        
        while puntos1 == puntos2:
            puntos1 += PuntosExtras()
            puntos2 += PuntosExtras()
        
        if puntos1 > puntos2:
            print(f"Set para {equipo1.nombre} ({puntos1} - {puntos2})")
            partido_terminado = RegistraSet(1)
        else:
            print(f"Set para {equipo2.nombre} ({puntos2} - {puntos1})")
            partido_terminado = RegistraSet(2)

def ResultadoTorneo():
    print("\n=== Resultado del Torneo ===")
    print(f"{equipo1.nombre}: {equipo1.partidosGanados} ganados, {equipo1.partidosPerdidos} perdidos")
    print(f"{equipo2.nombre}: {equipo2.partidosGanados} ganados, {equipo2.partidosPerdidos} perdidos")

def main():
    n = int(input("¿Cuántos partidos deben jugar los equipos?: "))
    for i in range(n):
        print(f"\n--- Partido {i + 1} ---")
        JugarPartido()
    ResultadoTorneo()

main()

