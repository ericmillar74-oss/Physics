import numpy
from matplotlib import pyplot as plt
import matplotlib.colors
from random import random

def f(r):
    x, y = r
    k = (1-x)**2 + 100*(y-x**2)**2
    return k
    
def grad(r):
    x, y = r
    dx = -2 + 2*x -400*x*y + 400*x**3
    dy = 200*(y-x**2)
    return numpy.array([dx,dy])

def gradientDescent(df, r0, eta, nstep):
    x,y = r0
    history = numpy.empty( (nstep+1, 2) )
    history[0] = r0
    for i in range (0,nstep):
        r0 = r0 - (eta*df(r0))
        history[i+1] = r0
    return history

N = 100 
x0 = -0.2
x1 = 1.2
y0 = 0
y1 = 1.2
xs = numpy.linspace(x0, x1, N)
ys = numpy.linspace(y0, y1, N)
dat = numpy.zeros((N, N))

for ix, x in enumerate(xs):
    for iy, y in enumerate(ys):
        r = [x,y]
        dat[iy, ix] = f(r)

plt.figure(figsize=(8,8))
im = plt.imshow(dat, extent=(x0, x1, y0, y1), origin='lower', cmap=matplotlib.cm.gray, 
                norm=matplotlib.colors.LogNorm(vmin=0.01, vmax=200))
plt.colorbar(im, orientation='vertical', fraction=0.03925, pad=0.04, label = '$f(x,y)$')

gammas = [0.004, 0.003, 0.002] 
r0 = numpy.array([0.2, 1]) 

for k in gammas:
    r = gradientDescent(grad, r0, k, 5000)
    plt.plot(r[:,0], r[:,1], marker = 'o', markersize = 5, label = "$\eta$ = {}".format(k))
plt.xlabel('$x$', fontsize = 12)
plt.ylabel('$y$', fontsize = 12)
plt.title('Gradient Descent to find minimum with different step sizes $\eta$ using 5000 steps')
plt.legend()
plt.show()
