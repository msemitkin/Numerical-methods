import math

def resolve(f, alpha, a, b, epsilon, x0):
    x1 = f(x0, alpha)
    print(x1)
    if(abs(x1 - x0) < epsilon):
        return x1
    elif(x1 > b or x1 < a):
        return None
    else:
        return resolve(f, alpha, a, b, epsilon, x1)

# x^4 - 3x^3 + 2
f = lambda x, alpha: alpha * (x**4 - 3*x**3 + 2) + x
alpha = -0.02
a = 2.0
b = 4.0
epsilon = 0.00001
x0 = (a+b) /2
print(resolve(f, alpha, a, b, epsilon, x0))
