#include <stdio.h>
#include <stdlib.h>
#include "wrapper.h"


int wrapper( float *vin, float *vout,  int size)
{
   /* for(int i = 0; i<size-1; i++)
    {
        for(int j = i+1; j< size; j++)
        {
            if(vin[i] == vin[j])
            {
                for(int k = j; k<size-1; k++)
                {
                    float aux;
                    aux = vin[k];
                    vin[k] = vin[k+1];
                    vin[k+1] = aux;
                }
                size--;
                j--;
            }
        }
    }*/
    
    for(int i=0;i<size;i++)
    {
        vout[i] = vin[i];
    }
    realloc(vout, size * sizeof(*vout));
    return 0;
}