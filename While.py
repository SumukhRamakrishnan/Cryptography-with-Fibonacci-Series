"""
 function to solve an equation in python. Initial attempts to solve an equation in Python.
"""

from gekko import GEKKO
m = GEKKO()
x = m.Var()
m.Equation(3* x + 1 ==2)
m.solve()
print(x.value)
