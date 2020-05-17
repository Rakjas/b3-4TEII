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
from mult import mult


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
    if len(sys.argv) != 2:
        print("Uso: {} scale".format(sys.argv[0]))
        sys.exit(0)
    # Escala N:
    try:
        N = float(sys.argv[1])
        if not (-5.0 <= N <= 5.0):
            raise ValueError()
    except:
        print("N must be a float value between -5.0 and +5.0")
        sys.exit(-1)

    # Generamos una serie aleatoria creciente, a partir de la suma acumulativa números aleatorios 
    # entre 0 y 1:
    SIZE = 50  # Tamaño del array.
    inp_arr = np.cumsum(np.random.rand(SIZE))
    out_arr = np.zeros_like(inp_arr)

    # Llamada a la función externa a través de su wrapper, con la correspondiente toma de tiempo:
    t0 = time.time_ns()
    out_arr = mult(inp_arr, N)
    t_exec = (time.time_ns()-t0)/1.0e9
    print("La función mult ha tardado {} segundos en ejecutarse.".format(t_exec))

    # Mostramos gráficas (de líneas y de barras) y terminamos:        
    plot_values(inp_arr, out_arr)
    show_plot_and_wait_for_key()
    plot_values(inp_arr, out_arr, line_else_bars=False)
    show_plot_and_wait_for_key()
 
if __name__ == '__main__':
    main()

