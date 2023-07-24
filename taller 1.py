# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class LecturaSensorError(Exception):
    pass

class SensorTemperatura:
    
    def leer_temperatura(self,temperatura):
        try:
            temperatura=int(temperatura)
            
        except:
            raise LecturaSensorError(" Error en el valor de temperatura ")
        
    def verificar_rango(self,temperatura):
        if int(temperatura)>=-50 and int(temperatura)<=100:
            print("Esta dentro del rango -50 a 100")
        else:
            raise LecturaSensorError("Error fuera de rango")

resp="s"
while resp=="s" or resp== "S":
    
    try:
        sensor=SensorTemperatura()
        temperatura=input("ingrese el valor de la temperatura: ")
        sensor.leer_temperatura(temperatura)
        sensor.verificar_rango(temperatura)
        print("desea ingresar otra temperatura s/n ")
        resp=input()
    except LecturaSensorError as e:
        print(e)
    
    
    
    