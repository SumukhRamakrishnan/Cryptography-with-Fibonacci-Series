"""
 It  computes the  determinant of a matrix M
"""

import numpy as np
from Message_Converter import n
def get_determinante(M):
    det = 0
    for array in M:
        det = M[0][0] * M[1][1] - M[0][1]*M[1][0]
    return det




