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
import numpy as np
import matplotlib.pyplot as plt



# Función auxiliar: muestra la figura matplotlib pendiente y espera una pulsación de tecla:
#@profile
def show_plot_and_wait_for_key():
    plt.draw()
    plt.pause(0.01)
    input("<Hit Enter To Close>")
    plt.close()


# Función auxiliar que muestra en matplotlib los arrays de entrada y de salida:
def plot_values(values_in, values_out, line_else_bars=True, width=0.5):
    if line_else_bars == True:
        plt.plot(values_in, color = 'r', label="Input values")
        plt.plot(values_out, color = 'g', label="Output values")        
    else:
        plt.bar(np.arange(len(values_in)) - width, values_in, width=width, color='r', 
                label="Input values")
        plt.bar(np.arange(len(values_out)), values_out, width=width, color='g', 
                label="Output values")

    plt.title('Matplotlib example (using {})'.format(["bars", "lines"][line_else_bars]))
    plt.legend()
    plt.xlabel('Array indices')
    plt.ylabel('Values')


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
        
    slist = sorted(lista)
    
    #parsing fEntrada
    try:
        for number in slist:
            N = int(number)
            if not (0 <= N <= 99999):
                raise ValueError()
    except:
        print("All values must be a int value between 0 and 99999")
        sys.exit(-1)
        
        
   
    #Creamos las soluciones
    
    #Método 1
    t0_sol1 = time.time_ns()
    sol1 = sorted(set(slist))
    texec_sol1 = (time.time_ns()-t0_sol1)/1.0e9
    
    print("La opcion 1: set ha tardado {} segundos en ejecutarse.".format(texec_sol1))
    
    #Método 2
    t0_sol2 = time.time_ns()
    sol2 = list(set(slist))
    texec_sol2 = (time.time_ns()-t0_sol2)/1.0e9
    
    
    print("La opcion 2: set ha tardado {} segundos en ejecutarse.".format(texec_sol2))
    
    #Guardamos la solucion
    
    try:
        name = sys.argv[2]
        file = open(name, "w")
        
    except:
        print("Can't create file")
        sys.exit(-1)

    for num in sol1:
        
        file.write(str(num))
       
    
    # Mostramos gráficas (de líneas y de barras) y continuamos:        
    print("Comenzamos el plot de las comparativas")
    
    plot_values(slist, sol1)
    show_plot_and_wait_for_key()
    plot_values(slist, sol1, line_else_bars=False)
    show_plot_and_wait_for_key()

 
if __name__ == '__main__':
    main()

