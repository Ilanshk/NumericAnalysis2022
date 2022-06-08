import math

import sympy as sp
from sympy.utilities.lambdify import lambdify
x = sp.symbols('x')
f = x**4 + x**3 - 3*x**2
first_derivative = sp.diff(f, x)
second_derivative = sp.diff(first_derivative,x)
print(f)
import math
print(first_derivative)
print(second_derivative)
second_derivative = lambdify(x,second_derivative)
values = [second_derivative(x) for x in range(-100,101)]
print(max(values))
epsilon = 0.000002


def find_number_of_partitions(start,end):
    value = epsilon*(12/(((end-start)**3)*10))
    return math.sqrt(1/value)



#print(find_number_of_partitions(0,math.pi))

def trapez(f,a,b,n):
    I = 0
    result = 0
    i = 0
    size = (b-a)/n    # גודל המקטע
    while i < n:
        result += (1/2)*(size)*(f(a)+f(a+size))
        a +=size
        i +=1
    return result



def simpson(f,a,b,n):
    h = (b-a)/n
    result = f(a)+f(b)
    size = (b-a)/n
    i=0
    a+=size
    while i < (n - 1):
        if i % 2 == 0:
            result += 4 * f(a)
        else:
            result += 2 * f(a)
        a += size
        i += 1
    return result*(1/3)*h






f = lambda x:sp.sin(x)
print(trapez(f,0,math.pi,find_number_of_partitions(0,math.pi)))
print(simpson(f,0,math.pi,4))

