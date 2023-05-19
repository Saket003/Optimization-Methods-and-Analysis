import numpy as np
# from helpers import round6
from fractions import Fraction


def tableau(A, b, c):
    m, n = A.shape

    # STEP 1 - Verify if works #TODO Not tested in frac case
    index_list = [index for index in range(len(b)) if b[index] < 0]
    for index in index_list:
        b[index] = -b[index]
        A[index, :] = -A[index, :]

    table = np.zeros((m+1, n+m+1), dtype=int) + Fraction()
    table[1:m+1, n+1:n+m+1] = np.eye(m, dtype=int) + Fraction()
    table[1:m+1, 1:n+1] = A
    table[1:m+1, 0] = b
    top_row = -1*table[:, 0:n+1].sum(axis=0)
    table[0, 0:n+1] = top_row[0:n+1]
    basis_list = np.arange(n+1, n+m+1, dtype=int)  # x1,x2,x3,x4

    # TODO - Verifying
    _, t2 = table.shape
    simplex_mod(table, t2-1, basis_list)

    # STEP 3 - Should be fine
    if (table[0, 0] > 0):
        return None, None, 1, None

    while (True):
        # STEP 4 - #TODO Verify
        if (abs(table[0, 0]) <= 1e-8 and np.all(basis_list < n+1)):  # TODO make 0 now
            x_opt = np.zeros(n, dtype=int) + Fraction()
            j = 1
            for i in basis_list:
                x_opt[i-1] = table[j, 0]  # basis_list indices x1,x2,x3,x4
                j += 1

            new_table = np.zeros((len(basis_list)+1, n+1),
                                 dtype=int) + Fraction()
            new_table[1:len(basis_list)+1, 0:n +
                      1] = table[1:len(basis_list)+1, 0:n+1]

            top_left = 0
            for var in basis_list:
                top_left += c[var-1]*x_opt[var-1]
            new_table[0, 0] = top_left

            c_b = np.zeros(len(basis_list), dtype=int) + Fraction()
            i = 0
            for var in basis_list:
                c_b[i] = c[var-1]
                i += 1

            for i in range(n):
                if (i+1 not in basis_list):
                    # TODO Verify
                    new_table[0, i+1] = c[i] - \
                        np.dot(c_b, table[1:len(basis_list)+1, i+1])
            return x_opt, new_table, 0, basis_list

        # STEP 5 - TODO Verify
        i = 0
        for var in basis_list:
            if (var > n):
                if (np.all(abs(table[i+1, 1:n+1]) <= 1e-6)):
                    table = np.delete(table, i+1, 0)
                    basis_list = np.delete(basis_list, i)
                else:
                    for it in range(1, n+1):
                        if (table[i+1, it] != 0):
                            buff = it
                            break
                    basis_list[i] = buff
                    table[i+1, :] = table[i+1, :]/table[i+1, buff]
                    for it in range(len(basis_list)):
                        if (it != i+1):
                            table[it, :] = table[it, :] - \
                                table[i+1, buff]*table[it, :]
                    i += 1
            else:
                i += 1


def simplex_mod(table, n, basis_list):
    a, b = table.shape
    while (True):
        x = table[0, 1:b]
        # x = round6(x)
        if np.all((x >= 0)):
            x_opt = np.zeros(n, dtype=int) + Fraction()

            l = 1
            for i in basis_list:
                x_opt[i-1] = table[l, 0]
                l += 1
            return x_opt, 0

        j = 0
        for i in range(b-1):
            if (x[i] < 0):
                j = i
                break
        j += 1  # In original table

        u = table[1:a, j]
        # u = round6(u)
        if np.all((u <= 0)):
            flag = 1
            return None, 1
        l = 0  # l in original table
        min_ratio = float("inf")  # TODO Verify
        for i in range(1, a):
            if (u[i-1] <= 0):
                continue
            ratio = table[i, 0]/u[i-1]
            # ratio = round(ratio,10)
            if (ratio < min_ratio):
                min_ratio = ratio
                l = i

        basis_list[l-1] = j
        # table[l,:] = Fraction(numerator=table[l,:],denominator=table[l,j])            #TODO Verify all together

        pivot = table[l, j]
        for i in range(b):
            table[l, i] = Fraction(numerator=table[l, i], denominator=pivot)

        for i in range(a):
            if (i == l):
                continue
            table[i, :] = table[i, :] - table[i, j]*table[l, :]


def dualsimplex(table, n, basis_list):
    # Verify whole pending
    a, b = table.shape
    while (True):
        x = table[1:a, 0]
        # x = round6(x)
        if np.all((x >= 0)):
            x_opt = np.zeros(n, dtype=int) + Fraction()

            j = 1
            for i in basis_list:
                x_opt[i-1] = table[j, 0]  # basis_list indices x1,x2,x3,x4
                j += 1
            return x_opt, 0

        l = 0
        for i in range(a-1):
            if (x[i] < 0):
                l = i
                break
        l += 1  # In original table

        v = table[l, 1:b]
        # v = round6(v)
        if np.all((v >= 0)):
            flag = 1
            return None, 1

        j = 0  # j in original table
        min_ratio = float("inf")  # TODO Verify
        for i in range(1, b):
            if (v[i-1] >= 0):
                continue
            ratio = Fraction(numerator=table[0, i], denominator=abs(v[i-1]))
            if (ratio < min_ratio):
                min_ratio = ratio
                j = i

        # Pivot is (l,j) in initial table
        basis_list[l-1] = j
        # table[l,:] = Fraction(numerator=table[l,:],denominator=table[l,j])

        pivot = table[l, j]
        for i in range(b):
            table[l, i] = Fraction(numerator=table[l, i], denominator=pivot)

        for i in range(a):
            if (i == l):
                continue
            table[i, :] = table[i, :] - table[i, j]*table[l, :]
