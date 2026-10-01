import numpy
import numpy as np
from matplotlib import pyplot as plt 

class walker:
    def __init__(self,x0,ndim=1, step_size=1.0):
        self.pos=x0
        self.ndim=ndim
        self.possibleSteps=[]
        for i in range(ndim):
            step=numpy.zeros(ndim)
            step[i]= - step_size
            self.possibleSteps.append(numpy.array(step,dtype='f'))
            step[i]= + step_size
            self.possibleSteps.append(step.copy())
        self.npossible=len(self.possibleSteps)

    def pickStep(self):
        istep = numpy.random.choice(range(self.npossible))
        return self.possibleSteps[istep]
        
    def doSteps(self,n):
        positions=numpy.ndarray((n+1,self.ndim),dtype='f')
        positions[0] = self.pos
        for i in range (0,n):
            positions[i+1] = positions[i] + self.possibleSteps[numpy.random.choice(range(self.npossible))]
        return positions

nsteps = 1000
ys = numpy.empty((100,nsteps+1))
for i in range(100):
    w = walker(numpy.zeros(1))
    ys[i] = w.doSteps(nsteps)[:,0]
plt.plot(range(nsteps+1),np.average(ys, axis = 0), label = 'Average position $<x>$')
plt.plot(range(nsteps+1),np.average((ys)**2, axis = 0), label = 'Average position squared $<x^2>$')
plt.xlabel('Number of Steps (N)')
plt.ylabel('$x$ Position')
plt.title('$<x>$ and $<x^2>$ for 100 1D Walkers Against N')
plt.legend()

nsteps = 100
for k in range(1,5):
    ys = numpy.empty((400,nsteps+1,k))
    for i in range(400):
        w = walker(numpy.zeros(k),ndim = k)
        ys[i] = w.doSteps(nsteps)
    plt.plot(range(nsteps+1),np.average(np.sum((ys)**2, axis=2), axis = 0),label = "D = {}".format(k))

plt.xlabel('Number of Steps (N)')
plt.ylabel('$<x^2>$')
plt.title('$<x^2>$ for 400 Walkers in D Dimensions Against N')
plt.legend()

ndim = 2
nwalkers = 1000
rand_pos = numpy.random.uniform(size=(nwalkers, ndim))
colours = ['red','green', 'blue']
k500 = numpy.empty((1000,2))
k100 = numpy.empty((1000,2))
k10 = numpy.empty((1000,2))
for i in range(nwalkers):
    w = walker(rand_pos[i],ndim = 2, step_size = 0.05)
    k = w.doSteps(10)
    k10[i] = k[-1]
for i in range(nwalkers):
    w = walker(rand_pos[i],ndim = 2, step_size = 0.05)
    k = w.doSteps(100)
    k100[i] = k[-1]
for i in range(nwalkers):
    w = walker(rand_pos[i],ndim = 2, step_size = 0.05)
    k = w.doSteps(500)
    k500[i] = k[-1]
plt.figure(figsize=(18,6))
plt.subplot(1, 3, 1)
plt.xlabel("x Position")
plt.ylabel("y Position")
plt.title(f"Position of 1000 Walkers After 10 Steps")
plt.xlim((-3, 4))
plt.ylim((-3, 4))
plt.scatter(k10[:,0],k10[:,1] , color = colours[0], alpha = 0.4)
plt.subplot(1, 3, 2)
plt.xlabel("x Position")
plt.ylabel("y Position")
plt.title(f"Position of 1000 Walkers After 100 Steps")
plt.xlim((-3, 4))
plt.ylim((-3, 4))
plt.scatter(k100[:,0],k100[:,1] , color = colours[1], alpha = 0.4)
plt.subplot(1, 3, 3)
plt.xlabel("x Position")
plt.ylabel("y Position")
plt.title(f"Position of 1000 Walkers After 500 Steps")
plt.xlim((-3, 4))
plt.ylim((-3, 4))
plt.scatter(k500[:,0],k500[:,1] , color = colours[2], alpha = 0.4)
