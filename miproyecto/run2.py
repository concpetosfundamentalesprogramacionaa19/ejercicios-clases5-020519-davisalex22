"""
file: misvariables.py
autor: @David Salazar
"""
from misvariables import *

# Declaracion de variables e ingreso de valores

nota = input("Ingrese nota 1: ")
nota2 = input("Ingrese nota 2: ")

nota = int(nota)
nota2 = int(nota2)
# CONDICIONALES
if nota >= 18:
	print("%s, su valor de nota es %d" % (mensaje,nota))
else:
    print("%s, su valor de nota es %d" % (mensaje2,nota))

if nota2 >= 18:
	print("%s, su valor de nota es %d" % (mensaje,nota2))
else:
    print("%s, su valor de nota es %d" % (mensaje2,nota2))

