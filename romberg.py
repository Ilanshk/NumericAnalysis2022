import math

import sympy as sp
x = sp.symbols('x')

fp = sp.sin(x ** 2 + 2) - sp.ln(2 * x ** 5 - 3 * x) #function
start = 2.5 * math.pi
end = 5.6 * math.pi
n = 10

def rumberg(polinom, start, end, n):
    f = sp.lambdify(x, polinom)
    i = 0
    RArray = []
    #Building R Vector
    while i < n:
        sum = 0
        t = 0
        if i != 0:
            end_of_sum = (2 ** i) - 1
            sum_section_size = (end - start) / (end_of_sum + 1)
            curr_point = start + sum_section_size
            while t < end_of_sum:
                sum += 2 * f(curr_point)
                curr_point += sum_section_size
                t += 1
        sum = sum + f(start) + f(end)
        RArray.append((end - start) * (0.5 ** (i + 1)) * sum)
        i += 1
    print("\n")
    temp = []
    j = 1
    while j < n:
        i = 1
        while i < n - j + 1:
            temp.append(RArray[i] + (1 / ((4 ** j) - 1) * (RArray[i] - RArray[i - 1])))
            print(str(temp[i - 1]))
            i += 1
        j += 1
        RArray = temp.copy()
        temp.clear()
        print("-------")
    return RArray[0]

print("Integral by Rumberg method:")
print(rumberg(fp, start, end, n))