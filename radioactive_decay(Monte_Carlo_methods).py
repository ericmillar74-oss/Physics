import numpy
import numpy as np
from matplotlib import pyplot as plt 
import random

plt.rcParams['figure.figsize'] = [9, 5]

def has_transitioned(prob):
    r = random.random()
    if r < prob:
        x = True
    else:
        x = False
    return x

def evolveOne(currentState, rules):
    for (a,b,prob) in rules :
        if currentState == a:            
            if has_transitioned(prob):
                return b
    return currentState

def evolveMany(states, rules):
    newState = []
    for i in range (0,len(states)):
        k = evolveOne(states[i],rules)
        newState.append(k)
    return newState

def evolve_system(NA, NB, NC, rules, n_steps):
    state = (['A'] * NA)+(['B'] * NB)+(['C'] * NC)
    A_count = np.empty(n_steps+1,dtype=int)
    B_count = np.empty(n_steps+1,dtype=int)
    C_count = np.empty(n_steps+1,dtype=int)
    A_count[0]= NA
    B_count[0] = NB
    C_count[0] = NC
    for i in range(0,n_steps) :
        state = evolveMany(state,rules)
        A_count[i+1] = state.count('A')
        B_count[i+1] = state.count('B')
        C_count[i+1] = state.count('C')
    return A_count, B_count, C_count

n_steps = 200
t_total = 100
dt = t_total/n_steps
x1 = []
for i in range (0,n_steps+1):
    k = i*dt
    x1.append(k)

t_half_A = 10.1
t_half_B = 15.7 
t_half_C = 3.2

tau_A = t_half_A/np.log(2)
tau_B = t_half_B/np.log(2)
tau_C = t_half_C/np.log(2)

prob_A = dt/tau_A
prob_B = dt/tau_B
prob_C = dt/tau_C

rules = [('A','B',prob_A),('B','C',prob_B),('C','A',prob_C)]

a1, b1, c1= evolve_system(0, 0, 250, rules, n_steps)

x2 = []
for i in range (0,n_steps+1):
    k = (i*dt) + 100
    x2.append(k)

rules2 = [('A','B',prob_A),('B','C',prob_B),('C','A',0)]

a2, b2, c2 = evolve_system(a1[-1], b1[-1], c1[-1], rules2, n_steps)

X = np.concatenate((x1,x2),axis = 0)
A = np.concatenate((a1,a2),axis = 0)
B = np.concatenate((b1,b2),axis = 0)
C = np.concatenate((c1,c2),axis = 0)

plt.figure(figsize=(8, 6))
plt.plot(X,A,label = "A count")
plt.plot(X,B,label = "B count")
plt.plot(X,C,label = "C count")
plt.xlabel('Time (hours)')
plt.ylabel('Number of Nuclei')
plt.title('Number of Nuclei vs Time (neutron flux turned off at Time = 100)')
plt.legend()
plt.show()

nsim = 20
counts=numpy.zeros((nsim,2*n_steps+2))
for i in range(0,nsim) :
    n_steps = 200
    t_total = 100
    dt = t_total/n_steps
    x1 = []
    for l in range (0,n_steps+1):
        k = l*dt
        x1.append(k)

    t_half_A = 10.1
    t_half_B = 15.7 
    t_half_C = 3.2

    tau_A = t_half_A/np.log(2)
    tau_B = t_half_B/np.log(2)
    tau_C = t_half_C/np.log(2)

    prob_A = dt/tau_A
    prob_B = dt/tau_B
    prob_C = dt/tau_C

    rules = [('A','B',prob_A),('B','C',prob_B),('C','A',prob_C)]

    a1, b1, c1= evolve_system(0, 0, 250, rules, n_steps)
    
    x2 = []
    for m in range (0,n_steps+1):
        k = (m*dt) + 100
        x2.append(k)

    rules2 = [('A','B',prob_A),('B','C',prob_B),('C','A',0)]

    a2, b2, c2 = evolve_system(a1[-1], b1[-1], c1[-1], rules2, n_steps)

    X = np.concatenate((x1,x2),axis = 0)
    A = np.concatenate((a1,a2),axis = 0)
    B = np.concatenate((b1,b2),axis = 0)
    C = np.concatenate((c1,c2),axis = 0)
    counts[i] = numpy.full(2*n_steps + 2,A)
print("Average    ",np.average(counts,axis=0))


alpha = np.std(counts,axis=0)

print("Uncertainty",alpha)

plt.figure(figsize=(8, 6))
plt.errorbar(X,np.average(counts,axis=0),yerr = alpha)
plt.xlabel('Time (hours)')
plt.ylabel('Average Number of A Nuclei')
plt.title('Average A vs Time (neutron flux turned off at Time = 100)')
plt.show()
