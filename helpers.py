import numpy as np
import math
import fractions


'''
All Functions here are verified
'''
def takeinput(filename):
    with open(filename) as f:
        line = f.readlines()
        n,m = (line[0].strip()).split()
        n = int(n)
        m = int(m)

        b = (line[1].strip()).split()
        b = np.asarray(b,dtype=float)

        c = (line[2].strip()).split()
        c = np.asarray(c,dtype=float)
        c = -1*c

        A = np.zeros((m,n))
        for i in range(m):
            temp = (line[3+i].strip()).split()
            A[i,:] = np.asarray(temp,dtype=float)
    return A,b,c,n,m

def convert(A,new_n,c):
    m,n = A.shape
    A_new = np.zeros((m,new_n))
    A_new[0:m,0:n] = A
    A_new[0:m,n:new_n] = np.eye(m)

    c_new = np.zeros(new_n)
    c_new[0:len(c)] = c
    return A_new,c_new


def choice(x,val):  
    max_frac = 0
    max_index = 0
    for i in range(len(x)):
        if(frac(x[i])>max_frac):
            max_frac = frac(x[i])
            max_index = i+1
    # if(frac(val)>=max_frac):
    #     max_frac = frac(val)
    #     max_index = 0
    return max_index

def round6(x):
    for i in range(len(x)):
        #if(abs(x[i] - round(x[i]))<1e-5):
        #    x[i] = round(x[i])
        #else:
        x[i] = round(x[i],6)
    return x

def addcondition(table, index, basis_list):
    a,b = table.shape
    new_table = np.zeros((a+1,b+1))
    new_table[0:a,0:b] = table
    new_table[a,b] = 1
    basis_list = np.append(basis_list, b)
    for j in range(b):
        new_table[a,j] = -1*frac(table[index,j])
    return new_table,basis_list

def frac(x):
    return x - math.floor(x)