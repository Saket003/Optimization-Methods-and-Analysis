import numpy as np
import math
from fractions import Fraction


def takeinput(filename):
    with open(filename) as f:
        line = f.readlines()
        n, m = (line[0].strip()).split()
        n = int(n)
        m = int(m)

        b = (line[1].strip()).split()
        b = np.asarray(b, dtype=int) + Fraction()

        c = (line[2].strip()).split()
        c = np.asarray(c, dtype=int) + Fraction()
        c = -1*c

        A = np.zeros((m, n), dtype=int) + Fraction()
        for i in range(m):
            temp = (line[3+i].strip()).split()
            A[i, :] = np.asarray(temp, dtype=int) + Fraction()
    return A, b, c, n, m


def convert(A, new_n, c):
    m, n = A.shape
    A_new = np.zeros((m, new_n), dtype=int) + Fraction()
    A_new[0:m, 0:n] = A
    A_new[0:m, n:new_n] = np.eye(m, dtype=int) + Fraction()
    c_new = np.zeros(new_n, dtype=int) + Fraction()
    c_new[0:len(c)] = c
    return A_new, c_new


def choice(x):
    max_frac = 0
    max_index = 0
    for i in range(len(x)):
        if (frac(x[i]) > max_frac):
            max_frac, max_index = frac(x[i]), i+1
    return max_index


def addcondition(table, index, basis_list):
    a, b = table.shape
    new_table = np.zeros((a+1, b+1), dtype=int) + Fraction()
    new_table[0:a, 0:b] = table
    new_table[a, b] = 1
    basis_list = np.append(basis_list, b)

    row_no = np.where(basis_list == index)[0][0] + 1
    for j in range(b):
        new_table[a, j] = -1*frac(table[row_no, j])
    return new_table, basis_list


def frac(x):
    return Fraction(x) - int(math.floor(x))
