"""
file: misvariables.py
autor: @David Salazar
"""
# Declaracion de variables 
prec = 1200
# Ingreso de valores por teclado
edad = input("¿Ingrese su edad? \n")
edad = int(edad)
modalidad = input("Ingrese la modalidad de estudio (a)Distancia (b)Presencial\n")
# CONDICIONALES evaluacion de seguro
if (edad <= 20):
	seguro = 100
else:
    seguro= 150
# CONDICIONALES evaluacion modalidad del estudiante    
if (modalidad == "a"):
	ciclo = 10
	valor_seguro = seguro * ciclo
	valor_total = valor_seguro + (prec * ciclo)
else:
    ciclo = 8
    valor_seguro = seguro *ciclo
    valor_total = valor_seguro + (prec * ciclo)
# Presentacion en pantalla del valor a pagar por la carrera
print("El precio total de su carrera universitaria es de : %d" % valor_total)
