from helpers import takeinput, choice, addcondition, frac, round6, convert
from simplex_tableau import tableau, dualsimplex, simplex_mod
import math
import numpy as np
import fractions

def gomory(filename):   
    A,b,c,initial_n,initial_m = takeinput(filename)     #Take Inputs as Ax<=b - Verified
    n = initial_n + initial_m   #Converts to Ax=b - Verified
    A,c = convert(A,n,c)

    #TODO Verify #Check initial table wrongish?
    x_opt,table,flag,basis_list = tableau(A,b,c)
    x_opt, flag = simplex_mod(table,n,basis_list)
    if(flag == 1):
        return None
    
    x_opt = round6(x_opt)   #Verified
    a,b = table.shape
    for i in range(a):
        table[i,:] = round6(table[i,:])
    
    feasible = True
    while(feasible):
        if(np.all([abs(i - round(i))<1e-5 for i in x_opt[0:initial_n]])):    #TODO Verify
            x = x_opt[0:initial_n]
            for i in range(len(x)):
                x[i] = round(x[i])
            x = x.astype(int)
            x = x.tolist()
            return x
        x_opt = round6(x_opt)
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
        

# print(gomory("TC\TC1.txt")) #[1,1]
# print(gomory("TC\TC2.txt")) #[0,2] - #TODO getting [0,1]
# print(gomory("TC\TC3.txt")) #[0,2,0,0]
# print(gomory("TC\TC4.txt")) #[4,4]
print(gomory("TC\TC5.txt")) #[4,4]