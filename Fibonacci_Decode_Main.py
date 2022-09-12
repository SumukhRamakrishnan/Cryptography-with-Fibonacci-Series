"""
 It is  the main program for the decoding algorithm .
 It computes the R-Matrix as a 1st step . Then computes the e_i values for equation R.
 The equation R is solved to the values of x (the missing 3rd column using hte determinant values).
 Eliminate the determinant  column and recompute the Matrix D.
 The Matrix D is converted into a single-dimensional matrix .
 Ignore the trailing zeroes in the single-dimensional matrix and convert the numeric values to the corresponding Unicode character representation.
"""
import numpy as np
from sympy import solve
from sympy import Symbol
import gekko as GEKKO
from Message_Divisor import D
from Message_Converter import k, k_2, y, h, zero_array, n_int
from R_Matrix import R_n
#print("Matrix K:","\n",D)

P = []
h_new = int(2*h)
for i in range(0,y,1):
    x = Symbol("b_3")
    e_11 = R_n[0, 0] * D[i,1] + R_n[1,0] * D[i,2]
    #print("e_11:", e_11)
    e_22 = R_n[0, 1] * D[i,1] + R_n[1,1] * D[i,2]
    #print("e_22:", e_22)
    b = solve(e_11*(R_n[0,1]*x + R_n[1,1]*D[i,3])-e_22*(R_n[0,0]*x + R_n[1,0]*D[i,3])- (5*((-1)**(n_int+1))*D[i,0]),x)
    #print(b)
    P.append([D[i,1], D[i,2], (*map(int, b)), D[i,3]])

P = np.array(P)
#print(P)
O = []
for i in range(0,y,1):
    r = P[i,:]
    r.shape = (2,2)
    r = np.transpose(r)
    O.extend(r)
O = np.array(O)
O = np.transpose(O)

A = O.reshape(1,h_new)

B = np.array(A).tolist()[0]
zero_array = np.array(zero_array).tolist()
zeros = len(zero_array)
print("1-dimensional Matrix:", "\n", B)
C = []
for i in range(0,h_new,1):
    org_character = B[i] + 97 - n_int
    org_character = chr(org_character)
    C.extend(org_character)
C = np.array(C).tolist()
for i in range(0,zeros,1):
    C.pop()
str1 = ''.join(str(e) for e in C)
print("Decrypted Text: ", str1)

