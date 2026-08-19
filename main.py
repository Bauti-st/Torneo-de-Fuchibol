import tabulate
import colorama
import random


def ingresar_equipos():
    print("\n==> TORNEO DE FÙTBOL <==")
    print("\nIngrese el nombre de los equipos que participan")
    eq_1 = input("Ingrese el nombre del primer equipo: ")
    
    eq_2 = input("Ingrese el nombre del segundo equipo: ")
    while eq_2 == eq_1:
        print("ERROR, Haz puesto el mismo nombre")
        eq_2 = input("Ingrese nuevamente el nombre del segundo equipo: ")

    eq_3 = input("Ingrese el nombre del tercer equipo: ")
    while eq_3 == eq_1 or eq_3 == eq_2:
        print("ERROR, Haz puesto el mismo nombre")
        eq_3 = input("Ingrese nuevamente el nombre del tercer equipo: ")

    eq_4 = input("Ingrese el nombre del cuarto equipo: ")
