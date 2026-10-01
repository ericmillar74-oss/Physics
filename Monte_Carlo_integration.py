import numpy
import matplotlib.pyplot as plt

def integrate(npoints, dim):
    # the random numbers
    x = 0
    rs = numpy.random.uniform(-1, 1, size=(npoints,dim)) 
    mod = numpy.sum(rs**2,axis=1)
    for r in mod:
        if r <= 1:
            x += 1
    V = (x/npoints)*2**(dim)
    return V

print(integrate(10,3))

ns = [2**ii for ii in range(4,20)]
dimensions = range(2,7)
volumes = [numpy.pi,(4/3)*numpy.pi,(1/2)*numpy.pi**2,8./15.*numpy.pi**2,1./6.*numpy.pi**3]
plt.figure(figsize=(6,5))
for i,dim in enumerate(dimensions):
    errors = []
    for k in ns:
        error = abs((volumes[i] - integrate(k,dim))/volumes[i]) 
        errors.append(error)
    plt.loglog(ns, errors, linewidth=1.5, markersize=6, label = "D = {}".format(i+2))
plt.loglog(ns, 1/numpy.sqrt(ns), color = 'black', linewidth=3, markersize=6, label = '$N^{-1/2}$')
plt.xlabel("Number of Points (N)")
plt.ylabel("Integration Error")
plt.title("Log-Log Plot of Error in Volume vs N")
plt.tight_layout()
plt.legend()
plt.show()
