from helpers import takeinput, choice, addcondition, frac, isInt
from dual_simplex import dualsimplex
from simplex_tableau import tableau
import math
import numpy as np

def gomory(filename):   
    A,b,c = takeinput
    
    x_opt,table,flag = tableau(A,b,c)  
    feasible = True

    if(flag == 1):
        return None

    while(feasible and not(isInt(x_opt))):
        i = choice(x_opt)
        table = addcondition(table,i)
        x_opt, flag = dualsimplex(table)
        if(flag == 1):
            feasible = False

    if(feasible == True):
        return x_opt #TODO verify data type - # an array of n integers
    else:
        return None #TODO
    
'''
Check - Potential cycling? some preference
'''