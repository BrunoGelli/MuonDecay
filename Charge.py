import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.path as path
import matplotlib.patches as patches
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import csv
import time
from time import gmtime, strftime
import sys


i = 0
j = 0
event = np.ones((2500, 1))
EventAux = []
try:
    with open("EventsList.csv") as f:
        for line in f:
            EventAux.append(float(line))
            # print(len(EventAux),  EventAux[0])
            if int(len(EventAux)) - 1 == int(EventAux[0]):
                EventAux.pop(0)
                event = np.c_[event, EventAux]
                del EventAux[:]

except IOError:
    print("Cannot open file")
    sys.exit(1)

event = np.transpose(event)

print(len(event))

x = []
for i in range(2500):
    x.append(i/250)
fig = plt.figure()
ax = fig.add_subplot(1,1,1,)
_ = ax.plot(x,event[1][:])
plt. xlabel('Time (us)')
plt. ylabel('Voltage (mV)')
plt.show(block = True)
