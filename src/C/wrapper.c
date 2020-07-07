#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "wrapper.h"

#define MAX_NUMBER 99999

int wrapper( int *vin, int *vout,  int size)
{
    
    int array[MAX_NUMBER];
    memset(array,0,MAX_NUMBER*sizeof(int));

    //Recorremos la entrada y mapeamos los valores que leemos (0 o 1)
    for(int i = 0; i<size; i++)
    {
        array[vin[i]] = 1;
    }

    
    //Rellenamos la salida con los valores encontrados
    int newsize=0;
    int * aux;
    //iteramos array y si encontramos un 1 es que para esa posicion (i) se encontro un valor
    //que concuerda con el que escribimos e incrementamos newSize de la colleción
    for(int i=0;i<=MAX_NUMBER; i++)
    {
       if(array[i]==1){
           aux = &vout[newsize];
           aux[0] = i;
           newsize++;
        }
    }
    
    return newsize;
}
