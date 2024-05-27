from sympy import Matrix
import numpy as np
from numpy import linalg as LA
from math import *

def solve(A, B):
    if (LA.matrix_rank(A) != LA.matrix_rank(np.concatenate((A, B), axis=1))):  return -1
    try:
        out = LA.solve(A, B)
        return [out, True]
    except LA.LinAlgError:
        
        solution = LA.lstsq(A, B, rcond=None)[0]
        eqs = [[i for i in j] for j in np.array(Matrix(list(A)).rref()[0], float)]
        #print(eqs)
        free = set([i for i in range(len(eqs[0]))])
        base = []
        for i in range(len(eqs)):
            index = eqs[i].index(1)
            free = free.difference(set([index]))
            base.append(index)
        free = list(free)
        eqs = np.array(eqs, float)
        eqs_based = eqs[:,[base[0]]]
        for i in base[1::]:
            eqs_based = np.c_[eqs_based, eqs[:,[i]]]
        vectors = []
        for i in free:
            vectors.append(vector_mult(np.c_[eqs_based, eqs[:,[i]]]))
        for i in vectors:
            for j in range(len(i)):
                i[j] = i[j]/i[-1]
        out = np.zeros([len(vectors), len(eqs[0])], float)
        #print(out)
        #print(base, free)
        for i in range(len(out)):
            for j in range(len(out[i])):
                if (free[i] == j):
                    out[i][j] = 1
                if j in base:
                    out[i][j] = vectors[i][base.index(j)]
        
        return [solution.T, out, False]


def vector_mult(A):
  out = [None for i in range(len(A[0]))]

  for i in range(len(out)):
    out[i] = round(LA.det(np.delete(A, i, 1)), 8)
    if i%2==1:
      out[i] *= -1
  return out    

def main():
    A = np.array([[1,2,3,5,3],
                  [2,4,6,1,2],
                  [4,1,2,3,1],
                  [1,1,6,3,3]], float)
    B = np.transpose(np.array([[0,0,0,0]], float))
    #print(A)
    #print(B)
    #print(np.concatenate((A, B), axis=1))
    print(solve(A, B))
    pass

if __name__ == "__main__":
    main()
