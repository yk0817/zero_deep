import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

def tangent_line(f,x):
    d = numerical_diff(f,x)
    y = f(x) - d*x
    return lambda t: d*t + y #無影関数定義

x = np.arange(0.0, 20.0, 0.1) #start,end,step

tf = tangent_line(function_1,5)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1,5)
y2 = tf(x)

plt.plot(x,y)
plt.plot(x,y2)
plt.show()