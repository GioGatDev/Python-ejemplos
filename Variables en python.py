#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:26:59 2018

@author: giovannisilva
"""
import math
print("Variables en Python")
a=1
b=4
print("Suma de a + b = ", a+b)
#flotante
c=0.5
d=1.75
print("Suma de c + d = ", c+d)
print("El valor de pi es: ", math.pi)
print("Formato de decimales", '{0:.5g}'.format(math.pi) )
c=1
print("El nuevo valor de c:",c)
#Solicitar al usuario
#tipo string
nombre = input("Introduce tu nombre: ")
print("Hola",nombre)
apellido = input("Introduce tu apellido: ")
print("Saludos", nombre+" "+apellido)
#Tipo entero
integrantes = int(input("Número de integrantes: "))
print("Pago: ",integrantes*10)
#Tipo flotante 
costo = float(input("¿Cuál es el costo ? "))
print("El costo es: ",costo)