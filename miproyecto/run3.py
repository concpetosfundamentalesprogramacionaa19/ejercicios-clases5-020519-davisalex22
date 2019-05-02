"""
file: misvariables.py
autor: @David Salazar
"""
"""
nota mayor a 18: sobresaliente

nota mayor o igual a 16 y menor a 18: muy buena

nota mayor o igual a 13 y menor a 16: buena

nota menor a 13: insuficiente
"""

from misvariables import *
# Declaracion de variables e ingreso de valores
nota = input("Ingrese nota 1: ")
nota = int(nota)
# CONDICIONALES
if (nota >= 18):
	print("%s  - nota %d" % ("Sobresaliente",nota))
else:
    if (nota >= 16) & (nota < 18):
	    print("%s  - nota %d" % ("Muy buena",nota))
    else:
    	if (nota >= 13) & (nota < 16):
	        print("%s  - nota %d" % ("Buena",nota)
	        else:
	    	    print("%s   - nota %d" % ("Insuficiente",nota))    	


  

