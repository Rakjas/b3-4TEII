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

# Wrapper python para llamar a la función implementada en C.
def wrapper(vin, size):
    # Objeto correspondiente a la función dentro de la biblioteca.
    funcwrapper = LIBWRAPPER.wrapper

    # Prototipo de la función: dos arrays a floats, la longitud de los arrays y
    # el escalar de multiplicación. Observa que ctypes no define punteros a datos que
    # no sean c_char, c_wchar y c_void, por lo que hay que crearlos con POINTER. 
    funcwrapper.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_int]

    # Valor devuelto por la función (se puede eliminar, pues es el
    # comportamiento por defecto).
    funcwrapper.restype = ctypes.c_int

    # Puesto que ctypes espera que los dos primeros parámetros sean instancias
    # de punteros a c_float (es decir, instancias LP_c_float), según el
    # prototipo de la función, no podemos usar directamente ni vin ni vout (como
    # copia de vin), ya que esos elementos son de tipo List y no instancias de
    # LP_c_float. Lo que hacemos es definir salida como un array de valores
    # c_float, con tantos elementos como tiene vin. Observa que hacemos lo mismo
    # con el primer parámetro que se le pasa a la función, si bien, en este
    # caso, los valores deben ser los del vector de entrada.

    salida=(ctypes.c_float * size)()
    entrada =(ctypes.c_float * size)(*vin)
    # Llamada a la función de la biblioteca compartida.
    funcwrapper(entrada, salida, size)

    # Vamos a devolver un vector. Para eso, hacemos una copia del vector de
    # entrada. Podríamos devolver directamente «salida», pero sería un objeto de
    # ctypes tal y como lo hemos definido, con lo que una simple orden
    # «print(salida)» no nos mostraría su contenido sino su tipo. Queda más
    # "elegante" devolver algo como la entrada.
    vout=np.resize(vin.copy(), len(salida))

    # Copiamos a dicho vector de salida el resultado de la función.
    for i in range(len(vout)):
      vout[i]=salida[i]

    # Devolvemos el vector de salida.
    return vout

if __name__ == "wrapper":
    # Cargamos la biblioteca compartida en ctypes.
    LIBWRAPPER = ctypes.CDLL (os.path.abspath(os.path.join(os.path.dirname(__file__),  "./libwrapper.so.1")))

