import math

def resolve(f, a, b, epsilon):
    c = (a + b) / 2.0
    if(f(c) == 0 or b-a < epsilon):
        return c
    elif(f(a)*f(c) < 0):
        return resolve(f, a, c, epsilon)    
    else:
        return resolve(f, c, b, epsilon) 

f = lambda x: x**3 - x**2 - 1

a = 0
b = 4
epsilon = 0.00001

print(resolve(f, a, b, epsilon))