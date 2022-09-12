import math

n=10
y= math.floor(math.sqrt(n))
for i in range(2,y):
    a = 2
    while a^i < n:
        a = a+1
    print(a^i)