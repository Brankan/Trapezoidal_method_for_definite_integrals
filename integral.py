from sympy import *
import math
from sympy.abc import a, x, y
from sympy import init_printing

import matplotlib.pyplot as plt

f =input("Type function:")
a =int(input('a:'))
b =int(input('b:'))
n =int(input('m:'))
firstarr=[]
secondarr=[]
originf=[]
okand=[]

h = float(b - a) / n
s = 0.0
x=a
s += eval(f)/2.0
for i in range(1, n):
    x=a + i*h
    s += eval(f)
x=b
s += eval(f)/2.0

print('trapezoidal method: '+str(s*h))



x, y, z, t = symbols('x y z t')
ff=integrate(eval(f),x,)
print('Integral result: '+str(ff))
pprint(ff)
x=a
aend=eval(str(ff))
x=b
bend=eval(str(ff))
res=bend-aend
print('Integral result:'+str(res))

for xd in range(-200,200):
    firstarr.append(xd)
    x=xd
    originf.append(eval(str(ff)))
    okand.append(eval(f))
    b=x
    a=x-1
    h = float(b - a) / n
    s = 0.0
    x = a
    s += eval(f) / 2.0
    for i in range(1, n):
        x = a + i * h
        s += eval(f)
    x = b
    s += eval(f) / 2.0
    secondarr.append(s*h)


plt.plot(firstarr, originf, label='x+1')
plt.plot(firstarr, secondarr, label='Furje(x+1)')
plt.plot(firstarr, okand, label='2)')
plt.axis([-100, 100, -100, 100])
plt.show()
