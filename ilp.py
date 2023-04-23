from helpers import takeinput, choice, addcondition, frac, round6, convert
from dual_simplex import dualsimplex
from simplex_tableau import tableau
import math
import numpy as np

def gomory(filename):   
    A,b,c,initial_n,initial_m = takeinput(filename)     #Take Inputs as Ax<=b - Verified

    n = initial_n + initial_m   #Converts to Ax=b - Verified
    A,c = convert(A,n,c)

    #TODO Verify #Check initial table wrongish?
    x_opt,table,flag,basis_list = tableau(A,b,c)
    if(flag == 1):
        return None
    
    
    x_opt = round6(x_opt)   #Verified
    a,b = table.shape
    for i in range(a):
        table[i,:] = round6(table[i,:])
    
    feasible = True
    while(feasible):
        if(np.all([abs(i - round(i))<1e-5 for i in x_opt])):    #TODO Verify
            x = x_opt[0:initial_n]
            x = x.tolist()
            return x

        i = choice(x_opt,table[0,0])    #Verified
        table,basis_list = addcondition(table,i,basis_list)     #Verified

        n += 1
        x_opt, flag = dualsimplex(table,n,basis_list)   #TODO Verify
        if(flag == 1):
            return None
        
        x_opt = round6(x_opt)   #Verified
        a,b = table.shape
        for i in range(a):
            table[i,:] = round6(table[i,:])
        

print(gomory("TC\TC1.txt"))
