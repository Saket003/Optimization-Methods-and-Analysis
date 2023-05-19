import numpy as np
from testsimp import tableau, simplex_mod, dualsimplex
b = np.array([3.0,2.0,5.0,1.0],dtype=float)
A = np.array([[1,2,3,0],[-1,2,6,0],[0,4,9,0],[0,0,3,1]],dtype=float)
c = np.array([1,1,1,0],dtype=float)
x,table,flag,basis_list = tableau(A,b,c)
# print(x)
# print(table)
# print(flag)
# print(basis_list)

basis_list = [5,6,7]
A = np.array([[3.0,-0.75,20.0,-0.5,6.0,0.0,0.0,0.0],[0.0,0.25,-8.0,-1.0,9.0,1.0,0.0,0.0],[0.0,0.5,-12.0,-0.5,3.0,0.0,1.0,0.0],[1.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0]])
x_opt,flag = simplex_mod(A,7,basis_list)
# print(x_opt)

basis_list = [4,5,6]
n = 6
A = np.array([[0.0,-10.0,-12.0,-12.0,0.0,0.0,0.0],[20.0,1.0,2.0,2.0,1.0,0.0,0.0],[20.0,2.0,1.0,2.0,0.0,1.0,0.0],[20.0,2.0,2.0,1.0,0.0,0.0,1.0]])
x_opt,flag = simplex_mod(A,n,basis_list)
print(x_opt)

table = np.array([[0,1,1,0,0],[-2,-1,-2,1,0],[-1,-1,0,0,1]], dtype=float)
n = 4
basis_list = [3,4]
x_opt, flag = dualsimplex(table,n,basis_list)
# print(x_opt)

table = np.array([[0,2,6,10,0,0],[2,-2,4,1,1,0],[-1,4,-2,-3,0,1]], dtype=float)
n = 5
basis_list = [4,5]
x_opt, flag = dualsimplex(table,n,basis_list)
# print(x_opt)