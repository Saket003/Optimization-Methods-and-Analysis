from helpers import takeinput, choice, addcondition, frac, isInt
from dual_simplex import dualsimplex
from simplex_tableau import tableau
import math
import numpy as np

def gomory(filename):   
    #A,b,c = takeinput

    #Check Ax = b
    A = np.array([[5,7,4,3,1,0], [7,0,2,1,0,1]])
    b = np.array([14,10])
    c = np.array([-8,-11,-6,-4,0,0])
    
    x_opt,table,flag,basis_list = tableau(A,b,c)  
    feasible = True

    if(flag == 1):
        return None
    
    n = len(c)

    while(feasible):
        flag = True
        for i in range(len(x_opt)):
            x = x_opt[i]
            if(frac(x)>=1e-6 and frac(x)<=1-1e-6):
                flag = False
            else:
                x_opt[i] = round(x_opt[i])
        if(flag == True):
            break


        i = choice(x_opt)
        table,basis_list = addcondition(table,i,basis_list)
        n += 1
        x_opt, flag = dualsimplex(table,n,basis_list)
        if(flag == 1):
            feasible = False
            break
        
        print(x_opt)

    if(feasible == True):
        return x_opt #TODO verify data type - # an array of n integers
    else:
        return None #TODO
    
'''
Check - Potential cycling? some preference
'''

print(gomory("Yo"))