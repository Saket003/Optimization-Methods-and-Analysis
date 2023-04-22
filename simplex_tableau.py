import numpy as np

def tableau(A,b,c):
    #Solving the relaxation
    n = len(c)
    x = np.zeros(n)
    table = 0
    #TODO
    flag = 0
    #TODO flag = 1 for unbounded
    return x, table, flag, basis_list

def simplex(table,n,basis_list):
    a, b = table.shape
    while(True):
        x = table[0,1:b]
        if(x>=0).all():
            x_opt = np.zeros(n)

            l = 1
            for i in basis_list:
                x_opt[i-1] = table[l,0]
                l += 1
            return x_opt, 0
            
            j = 0
        for i in range(b-1):
            if(x[i]<0):
                j = i
                break       #Verify cycling
        j += 1 #In original table

        u = table[1:a,j]
        if (u<=0).all():
            flag = 1
            return None, 1
        l = 0 #l in original table
        min_ratio = float("inf")
        for i in range(1,a):
            if(u[i-1]<=0):
                continue
            ratio = table[i,0] / u[i-1]
            if(ratio<min_ratio):
                min_ratio = ratio
                l = i

        basis_list[l-1] = j
        table[l,:] = table[l,:]/table[l,j]
        for i in range(a):
            if(i == l):
                continue
            table[i,:] = table[i,:] - table[i,j]*table[l,:]

        print(table)

'''basis_list = [4,5,6]
n = 6
A = np.array([[0.0,-10.0,-12.0,-12.0,0.0,0.0,0.0],[20.0,1.0,2.0,2.0,1.0,0.0,0.0],[20.0,2.0,1.0,2.0,0.0,1.0,0.0],[20.0,2.0,2.0,1.0,0.0,0.0,1.0]])
x_opt,flag = simplex(A,n,basis_list)
print(x_opt)

basis_list = [5,6,7]
A = np.array([[3.0,-0.75,20.0,-0.5,6.0,0.0,0.0,0.0],[0.0,0.25,-8.0,-1.0,9.0,1.0,0.0,0.0],[0.0,0.5,-12.0,-0.5,3.0,0.0,1.0,0.0],[1.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0]])
x_opt,flag = simplex(A,7,basis_list)
print(x_opt)'''