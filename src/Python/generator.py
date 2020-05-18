#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:55:43 2020

@author: luis
"""
import numpy as np
import sys

def main():   
    # Control de argumentos de línea de comandos:
    if len(sys.argv) != 2:
        print("Uso: {} nombreFichero".format(sys.argv[0]))
        sys.exit(0)
    
    try:
        name = sys.argv[1]
        file = open(name, "w")
        
    except:
        print("Can't create file")
        sys.exit(-1)


    #Generamos el array de valores
    SIZE = 200000  # Tamaño del array.
    arr = np.random.rand(SIZE) * 99999
    
    #Lo guardamos en file
    for x in arr:
        numero = int(x)
        file.write(str(numero))
        file.write("\n")
    
    file.close
    
    
if __name__ == '__main__':
    main()