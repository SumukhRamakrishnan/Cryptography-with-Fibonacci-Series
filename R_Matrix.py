"""
 It is used by the decryption function to construct  the  R-MATRIX .
"""
import numpy as np
from sympy import solve
from sympy import Symbol
from Message_Converter import*
#from Fibonacci_Key_Main import matrix
from Matrices import get_determinante
from Message_Divisor import D

def fibonacci_sequences(f):
    if n_int==0:
        print("Not possible")
    a = 0
    b = 1
    for i in range(f-1):
        a,b = b,b+a
    return b
#print(n_int)
f_n1 = fibonacci_sequences(n_int+1)
#print(f_n1)
f_n0 = fibonacci_sequences(n_int)
#print(f_n0)
f_nminus1 = fibonacci_sequences(n_int-1)
if n_int == 1:
    f_nminus1 = 0
#print(f_nminus1)

R = np.array([[1,2],[2,-1]])
Q_n = np.array([[f_n1,f_n0],[f_n0,f_nminus1]])
#print(Q_n)
R_n = R.dot(Q_n)
R_n = np.array(R_n)
print("Matrix R_n:", "\n", R_n)

# coding and testing the algorithm for constructing the R-Matrix with specific values

'''b = side_length(len_a_in)
print(A_slice)
detR_n = get_determinante(R_n)
print(get_determinante(R_n))
import gekko as GEKKO
for i in range(0,4,1):
    m = GEKKO()
    x = m.Var()
    e_i1 = R_n[0,0] * A_slice[i,0] + R_n[1, 0] * A_slice[i, 1]
    e_i2 = R_n[0, 1] * A_slice[i, 1] + R_n[1, 1] * A_slice[i, 1]
    print(e_i2)
    print(e_i1)
    r = get_determinante(R_n)
    d = P[0,i]
    m.Equation(e_i1*R_n[0,1]*x + e_i1*R_n[1,1]*A_slice[i,4] - e_i2*R_n[0,0]*x + e_i2*R_n[1,0]*A_slice[i,4] == r * d)
    m.solve()
    print(x.value)'''

'''while i <=y-1:
    Slice = P[i,:]
    H = Slice.reshape(2,2)
    N.append(H[0,:])
    M.append(H[1,:])
    i = i+1'''

'''M, N = np.array(M), np.array(N)
M.reshape(1,h)
N.reshape(1,h)
print("M:", M)
print("N:",N)'''

