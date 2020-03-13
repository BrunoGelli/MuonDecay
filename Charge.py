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


def plotdata(data, points, peak):
    x = []
    for i in range(2500):
        x.append(i)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, )
    _ = ax.plot(x, data)
    _ = ax.plot(points, peak, 'ro')
    plt.xlabel('Time (us)')
    plt.ylabel('Voltage (mV)')
    plt.show(block=True)
    return


def integrate(data, points, size):
    charge = np.zeros(len(points))
    for peaknumber in range(len(points)):
        for iterator in range(points[peaknumber] - size, points[peaknumber] + size, 1):
            charge[peaknumber] = charge[peaknumber] + data[iterator]
    return charge


event = np.ones((2500, 1))
EventAux = []
try:
    with open("EventsList.csv") as f:
        for line in f:
            EventAux.append(float(line))
            if int(len(EventAux)) - 1 == int(EventAux[0]):
                EventAux.pop(0)
                event = np.c_[event, EventAux]
                del EventAux[:]

except IOError:
    print("Cannot open file")
    sys.exit(1)

event = np.transpose(event)
event = event[1:]

charge = []

for i in range(len(event)):
    peaks, h = find_peaks(event[i][:], height=0, distance=10)
    # plotdata(event[i][:], peaks, h.get('peak_heights'))
    charge.append(integrate(event[i][:], peaks, 5))


print(charge)
charge = np.transpose(charge)
print(charge)

_ = plt.hist(charge[0], bins='auto')
plt.title('Charge of the first pulse')
plt.show(block=True)

_ = plt.hist(charge[1], bins='auto')
plt.title('Charge of the second pulse')
plt.show(block=True)