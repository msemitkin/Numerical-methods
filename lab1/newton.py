import math

def resolve(f, f_, epsilon, x_0):
    if(f(x_0) < epsilon):
        return x_0
    x_1 = x_0 - f(x_0) / f_(x_0)
    return resolve(f, f_, epsilon, x_1)


f = lambda x: x**3 - x**2 - 1
f_ = lambda x: x * (3*x - 2)
f__ = lambda x: 6*x - 2

a = 0
b = 5
epsilon = 0.0000001

x_0 = b if f(b)*f__(b) > 0 else a
print(resolve(f, f_, epsilon, x_0))
