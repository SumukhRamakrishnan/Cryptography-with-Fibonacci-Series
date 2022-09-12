"""
The Message divisor is used by the encryption algorithm.
It slices the one-dimensional matrix into a 2-dimensional matrix D.
It divides them into block matrices B.

"""
import array as arr
import numpy as np
from Message_Converter import A_slice, b_tobeslicedup, h
from Matrices import get_determinante

Array_new = [[A_slice.item(0,0),A_slice.item(0,1)],[A_slice.item(1,0),A_slice.item(1,1)]]
Array_new = np.matrix(Array_new)
#print(Array_new)
#creating block matrices
i,j,z = 0,0, 0
D = []
while i <= h-1:
    Array_new =[[b_tobeslicedup.item(0,i),b_tobeslicedup.item(0,i+1)], [b_tobeslicedup.item(1,i),b_tobeslicedup.item(1,i+1)]]
    #print(Array_new)
    det1 = get_determinante(Array_new)#determinant of the block matrix
    #print("Determinant:",det1)
    Array_new2 = [det1, b_tobeslicedup.item(0,i),b_tobeslicedup.item(0,i+1), b_tobeslicedup.item(1,i+1)]
    D.append(Array_new2)
    i= i+2
D = np.array(D)
D.transpose()
print("Encrypted matrix K:", "\n",D)

#coding and testing with specific values the algorithm for message divisor.
#getting the determinants of the block matrices
"""
Decoding Algorithm using Lucas Blocking algorithm before modification.
This version only worked for text length between five and sixteen characters long.
"""

'''while i <= k + 1:
    while j <= k+1:
        Array_new = [[A_slice.item(0, j), A_slice.item(0, j + 1)], [A_slice.item(1, j), A_slice.item(1, j + 1)]]
        j = j+2
        print(Array_new)
        det1 = get_determinante(Array_new)
        P.append(det1)
        print(det1)
        #print(P)
    Array_new = [[A_slice.item(2, i), A_slice.item(2, i+1)], [A_slice.item(3, i), A_slice.item(3,i+1)]]
    i=i+2
    det1 = get_determinante(Array_new)
    P.append(det1)
    print(det1)
for i in range(0,4,1):
    b = A_slice[i,:]
    c = b.reshape(2,2)
    Array_new = [[c.item(0,0), c.item(0,1)],[c.item(1,0), c.item(1,1)]]
    print(Array_new)
    d = np.bmat(c)
    print(d)
    D.append(d)
matrix = np.bmat([[D[0] ,D[1] ],[D[2], D[3]]])
P = np.matrix(P)'''

'''
print(matrix)
print(P)
def get_encryp(P,matrix):
    P2d = P[:, np.newaxis]
    P2d = np.matrix(P2d)
    P2d = P2d.transpose()
    matrix[:,0] = P2d[:,0]
    return matrix[:,0]

'''

