import tabulate
import colorama
import random as ram
import time

def ingresar_equipos():
    equipos = []
    palabras = ["primer", "segundo", "tercero", "cuarto"]
    print("\n==> TORNEO DE FÙTBOL <==")
    print("\nIngrese el nombre de los equipos que participan")

    for i in range(4):
        eq = input(f"Ingrese el nombre del {palabras[i]} equipo: ")
        while eq in equipos:        
            print("===            ‼️ERROR‼️            ===")
            print("Ya has ingresado a ese equipo antes...")
            eq = input("Vuelva a ingresar al eqipo (uno que no hayas puesto antes): ")
        
        equipos[eq] = {"Goles a favor":0, "Ganados":0, "Empatados":0, "Perdidos":0, "Puntos":0}
    
    return equipos

def simular_partidos(equipos):
    print("=== PRIMER PARTIDO ===")
    print(f"Se enfrentarán {equipos[0]} contra {equipos[1]}")
    time.sleep(0.3)
    print("⌚¡ARRANCÓ EL PARTIDOOO!")
    time.sleep(0.5)
    print("FINALIZÓ EL PARTIDOOO")
    gol_1 = ram.randint(0, 5)
    gol_2 = ram.randint(0, 5)
    time.sleep(0.2)
    if gol_1 > gol_2:
        print("GANOOOO", {equipos[0]})
    else:
        print("GANOOOO", {equipos[1]})
    time.sleep(0.2)
    print("----->             RESULTADO            <-----")
    time.sleep(0.1)
    print(f"{equipos[0]}: {gol_1} - {gol_2} :{equipos[1]}")

def armar_fixture(equipos):
    for i in range(12):
        ram.choice(equipos)
        fixture = {}