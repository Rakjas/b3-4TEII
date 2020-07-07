#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:22:59 2020

@author: luis
"""


'''
Práctica TEII - Bloque 4 - Código de la sesión 3 de prácticas
'''

import sys
import time
import ctypes
import numpy as np
import matplotlib.pyplot as plt
from wrapper import wrapper 
from matplotlib.backends.backend_pdf import PdfPages

MAX_NUMBER = 99999

# Función auxiliar: muestra la figura matplotlib pendiente y espera una pulsación de tecla:
#@profile
def show_plot_and_wait_for_key():
    
    plt.show()
    input("<Hit Enter To Close>")
    plt.close()

    
# Función auxiliar que muestra en matplotlib los arrays de entrada y de salida:
def plot_values(values_in1, values_in2, values_in3, name, line_else_bars=True, width=0.5):
    f = plt.figure()
    if line_else_bars == True:
        plt.plot(values_in1, color = 'r', label="Set")
        plt.plot(values_in2, color = 'g', label="Diccionario") 
        plt.plot(values_in3, color = 'b', label="Método implementado") 
    else:
        plt.bar(np.arange(len(values_in1)) - width, values_in1, width=width, color='r', 
                label="Set")
        plt.bar(np.arange(len(values_in2)), values_in2, width=width, color='g', 
                label="Diccionario")
        plt.bar(np.arange(len(values_in3)), values_in3, width=width, color='b', 
                label="Método implementado")

    plt.title('Comparativa del tiempo consumido entre los distintos métodos'.format(["bars", "lines"][line_else_bars]))
    plt.legend()
    plt.xlabel('CasosConsiderados * 2000')
    plt.ylabel('Segundos')
    f.savefig(str(name + ".pdf"),bbox_inches='tight')


# Código main:
def main():   
    # Control de argumentos de línea de comandos:
    if len(sys.argv) != 4:
        print("Uso: {} ficheroEntrada, ficheroSalida, pdfLogFile".format(sys.argv[0]))
        sys.exit(0)
        
    #reading fEntrada
    try:
        f = open(sys.argv[1])
        lista = f.readlines()
    except:
        print("No se encuentra el archivo de Entrada")
        sys.exit(-1)
       
    
    #parsing fEntrada, check for incorrect values
    try:
        for number in lista:
            N = int(number)
            if not (0 <= N <= 99999):
                raise ValueError()
    except:
        print("All values must be a int value between 0 and 99999")
        sys.exit(-1)
        
    #inicializamos marcadores de tiempo
    timeOption1 = []
    timeOption2 = []
    timeOption3 = []
    
    #Creamos las soluciones
    for i in range(2000,200000,2000):
        #Método 1, usando el metodo set de python
        t0_sol1 = time.time_ns()
        sol1 = list(set(lista[0:i]))
        texec_sol1 = (time.time_ns()-t0_sol1)/1.0e9
        
        #Método 2, usando diccionarios en python
        aux = 0
        t0_sol2 = time.time_ns()
        sol2 = list(dict.fromkeys(lista[0:i], 0))
        texec_sol2 = (time.time_ns()-t0_sol2)/1.0e9
        
        #Método 3, definido en c y llamado a través del wrapper
        arrayAux = (ctypes.c_int * MAX_NUMBER)(*np.zeros(MAX_NUMBER, dtype=int))
        listTarget = lista[0:i].copy() 
        listTarget = [int(i) for i in listTarget]
        sol3 = np.zeros_like(listTarget)
        t0_sol3 = time.time_ns()
        sol3 = wrapper(listTarget,i, arrayAux)
        texec_sol3 = (time.time_ns()-t0_sol3)/1.0e9
        
        #Comprobamos que los 3 metodos den la misma solucion
        try:
            if not (len(sol1)==len(sol2)==len(sol3)):
                 raise ValueError()
        except:
            print("Los métodos difieren en el resultado")
            sys.exit(-1)
        
        #Guardamos los datos para esta iteracion, para poder dibujarlos con matplotlib
        timeOption1.append(texec_sol1)
        timeOption2.append(texec_sol2)
        timeOption3.append(texec_sol3)
    
    #Creamos el archivo solucion
    try:
        name = sys.argv[2]
        file = open(name, "w")
        
    except:
        print("Can't create file")
        sys.exit(-1)

    for num in sol1:
        
        file.write(str(num))
       
        
    # Guardamos los graficos en el pdf de salida marcado
    
    plot_values(timeOption1, timeOption2, timeOption3, sys.argv[3])
    
    show_plot_and_wait_for_key()
    


 
if __name__ == '__main__':
    main()

