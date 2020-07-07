#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "wrapper.h"

#define MAX_NUMBER 99999

int wrapper( float *vin, float *vout,  int size, int *array)
{
    
    //int array[MAX_NUMBER];
    //memset(array,0,MAX_NUMBER*sizeof(int));

    //Recorremos la entrada y mapeamos los valores que leemos (0 o 1)
    for(int i = 0; i<size; i++)
    {
        array[(int)vin[i]] = 1;
    }

    
    //Rellenamos la salida con los valores encontrados
    float newsize=0;
    float * aux;
    //iteramos array y si encontramos un 1 es que para esa posicion (i) se encontro un valor
    //que concuerda
    for(int i=0;i<=MAX_NUMBER; i++)
    {
       if(array[i]==1){
           aux = &vout[(int)newsize];
           aux[0] = i;
           newsize++;
        }
    }
    
    return newsize;
}
