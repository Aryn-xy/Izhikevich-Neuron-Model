import numpy as np
import matplotlib.pyplot as plt

t=300
dt=1
time = np.arange(0,t+dt,dt)
a = 0.02
b = 0.2
c = -65
d = 8
I = 10

v = np.full(len(time), -65.0)  
u = np.zeros(len(time))        
u[0] = b * v[0]               

for t in range(1, len(time)):
    #Izhikevich model equation
    v[t] = v[t-1] + (0.04*v[t-1]**2 + 5*v[t-1] + 140 - u[t-1] + I)*dt
    u[t] = u[t-1] + a*(b * v[t-1] - u[t-1])* dt
   
    if v[t] >= 30:
        v[t] = c            #reset v after spike
        u[t] += d           #increase recovery variable

plt.plot(time, v)
plt.title("Izhikevich Neuron Model Simulation")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.show()
