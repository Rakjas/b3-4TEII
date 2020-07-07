#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:30:30 2020

@author: luis
"""

'''
Wrapper python para llamar a la función implementada en C.

Observación: no podemos llamar a este fichero libmult.py, por ejemplo. Si lo
hacemos, la orden «import libmult» pensará que se trata de un módulo nativo de
Python y dará un error al no encontrar definida una función llamada
PyInit_libmult.
'''
import ctypes, os
import numpy as np


#@profile
# Wrapper python para llamar a la función implementada en C.
def wrapper(size, entrada, salida):
    # Objeto correspondiente a la función dentro de la biblioteca.
    funcwrapper = LIBWRAPPER.wrapper

    # Prototipo de la función: dos arrays a floats, la longitud de los arrays y
    # un array auxiliar.

    funcwrapper.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]

    # Valor devuelto por la función (se puede eliminar, pues es el
    # comportamiento por defecto).
    funcwrapper.restype = ctypes.c_int

    # Llamada a la función de la biblioteca compartida.
    newSize = funcwrapper(entrada, salida, size)


    salida = np.resize(salida, newSize)
    return salida
   

if __name__ == "wrapper":
    # Cargamos la biblioteca compartida en ctypes.
    LIBWRAPPER = ctypes.CDLL (os.path.abspath(os.path.join(os.path.dirname(__file__),  "../C/libwrapper.so.1")))

