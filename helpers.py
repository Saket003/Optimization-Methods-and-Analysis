import numpy as np
import math

def takeinput(filename):
    n = 5#TODO 
    m = 5#TODO

    # Take input from file "filename" string
    # Check input order
    #TODO
    b = np.zeros((m,1)) #make 1d
    c = np.zeros(n)
    A = np.zeros((m,n))

    return A,b,c

def choice(x):  
    '''
    Choose a source row i
    Taking largest fractional part and lower index for tiebreaker
    '''
    max_frac = 0
    max_index = 0
    for i in range(len(x)):
        frac = x[i] - math.floor(x[i])
        if(frac>max_frac):
            max_frac = frac
            max_index = i
    return max_index

def addcondition(table, index, basis_list):
    a,b = table.shape

    new_table = np.zeros((a+1,b+1))
    new_table[0:a,0:b] = table
    #TODO Verify
    new_table[a,b] = 1      #Adding 1 corresponding to new basic variable S

    basis_list = np.append(basis_list, b)
    #add generated gomory cut
    for j in range(b):
        new_table[a,j] = -1*frac(table[index,j])
    return new_table,basis_list

def frac(x):
    return x - math.floor(x)

def isInt(x):
    '''
    X is a nd.array, checks all elements
    '''
    flag = True
    for val in x:
        if(frac(val)!=0):
            flag = False
            break
    return flag