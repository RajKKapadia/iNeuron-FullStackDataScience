'''Use this to solve Quadratic Equation
   Example: ax^2 + bx + c
   then enter: a-b-c
'''
import cmath
e = input('Enter equation: ')

e = e.split('-')

a = int(e[0])
b = int(e[1])
c = int(e[2])

s = []

d = b ** 2 - 4*a*c

s.append((-b + cmath.sqrt(d)) / 2*a)
s.append((-b - cmath.sqrt(d)) / 2*a)

print(f'The roots of the equation {a}X^2+{b}X+{c} are {s[0]} and {s[0]}.')
