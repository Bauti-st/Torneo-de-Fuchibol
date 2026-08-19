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
    #hacer la simulaciòn de los partidos
    pass

def armar_fixture(equipos):
    fixture =  {"Fecha 1": [(equipos[0], equipos[1]), (equipos[3], equipos[2])],
                    "Fecha 2": [(equipos[2], equipos[0]), (equipos[1], equipos[3])],
                    "Fecha 3": [(equipos[0], equipos[3]), (equipos[2], equipos[1])],
                    "Fecha 4": [(equipos[1], equipos[0]), (equipos[3], equipos[2])],
                    "Fecha 5": [(equipos[0], equipos[2]), (equipos[3], equipos[1])],
                    "Fecha 6": [(equipos[0], equipos[3]), (equipos[1], equipos[2])]
        }
    
    return fixture