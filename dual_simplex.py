import numpy as np

def dualsimplex(table,n,basis_list):
    a,b = table.shape
    while(True):    
        x = table[1:a,0]
        if np.all((x>=0)):
            x_opt = np.zeros(n)

            j = 1
            for i in basis_list:
                x_opt[i-1] = table[j,0] #basis_list indices x1,x2,x3,x4
                j += 1
            return x_opt, 0

        l = 0
        for i in range(a-1):
            if(x[i]<0):
                l = i
                break       #Verify cycling
        l += 1 #In original table

        v = table[l,1:b]
        if np.all((v>=0)):
            flag = 1
            return None, 1
        
        j = 0 #j in original table
        min_ratio = float("inf")
        for i in range(1,b):
            if(v[i-1]>=0):
                continue
            ratio = table[0,i]*round(1/abs(v[i-1]),10)
            if(ratio<min_ratio):
                min_ratio = ratio
                j = i

        #Pivot is (l,j) in initial table
        basis_list[l-1] = j
        table[l,:] = table[l,:]*round(1/table[l,j],10)
        for i in range(a):
            if(i == l):
                continue
            table[i,:] = table[i,:] - table[i,j]*table[l,:]

        #print(table)

'''
basis_list = [4,5]
n = 5
A = np.array([[0.0,2.0,6.0,10.0,0.0,0.0],[2.0,-2.0,4.0,1.0,1.0,0.0],[-1.0,4.0,-2.0,-3.0,0.0,1.0]])

x_opt,flag = dualsimplex(A,n,basis_list)
print(x_opt)
#[0.  0.5 0.  0.  0. ]

basis_list = [3,4]
n = 4
A = np.array([[0.0,1.0,1.0,0.0,0.0],[-2.0,-1.0,-2.0,1.0,0.0],[-1.0,-1.0,0.0,0.0,1.0]])

x_opt,flag = dualsimplex(A,n,basis_list)
print(x_opt)
#[1.  0.5 0.  0. ]
'''