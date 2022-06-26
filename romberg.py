import sympy as sp
from sympy.utilities.lambdify import lambdify


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


def Romberg():
    T = []
    TR = []
    g = 1
    count = 8
    n = 1
    c= 0
    while g < count:
        T.append(trapez(f, 0, 1, n))
        print("%f "% (trapez(f, 0, 1, n)))
        c+=1
        g += 1
        n *= 2
        for i in range(c):
            for j in range(c,-1,-1):
                TR.append(T[:i]+)(1/())



      # ''' T.append(trapez(f, 0, 1, n))
      #   count = T[:-1] - T[]'''








x = sp.symbols('x')
my_f = 1/(2+ x**4)
print("my_func: ", my_f)
my_f1= sp.diff(my_f, x)
#print("f' : ", my_f1)

d1 = sp.diff(my_f1,x)
#print("f'': ", d1)

#calc the derivative from func -> lambdify
f =  1/(2+ x**4)
f_prime = f.diff(x)
print("f : ",f)
#print("f' : ",f_prime)
f = lambdify(x, f)
f_prime = lambdify(x, f_prime)
d1 = lambdify(x,d1)
Romberg()