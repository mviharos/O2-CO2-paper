import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import os
from os.path import exists
from scipy.optimize import curve_fit

def func(x, a, c, d):
    return a*np.exp(-c*x)+d


def Leg1():
    m2 = mpatches.Patch(color='indianred', label='Under 30 years')
    m3 = mpatches.Patch(color='maroon', label='Over 70 years')
    plt.legend(ncol=1,handles=[m3,m2],bbox_to_anchor=(0.3, 0.87), loc='center',fontsize=10)

def Leg2():
    m0 = mpatches.Patch(color='darkslategrey', label='Woman')
    m1 = mpatches.Patch(color='teal', label='Man')
    plt.legend(ncol=1,handles=[m0,m1],bbox_to_anchor=(0.3, 0.87), loc='center',fontsize=10)

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


def abrazol(t,val, title):

    plt.scatter(t, val,color='darkslategrey',s=50)
    plt.grid()
    plt.xlabel("Multiplicator of nominal grid points [1]")
    plt.title(title,fontsize=13)
    plt.ylabel("Normalised transport variable [1]")



fig, ax = plt.subplots(1, 2, figsize=(10,4))
fig.tight_layout(pad=1.)
plt.subplots_adjust(left=0.1,
                    bottom=0.05,
                    right=0.92,
                    top=0.95,
                    wspace=0.3,
                    hspace=0.35)

T = 75.

ax1 = fig.add_subplot(ax[0])
data = pd.read_csv(os.path.join("results//Abel_ref2//arterial//A12.txt"),header=None)
t = data[0]
y = data[1]
plt.plot(t,y)

data = pd.read_csv(os.path.join("results//Abel_ref2//arterial//A12.txt"),header=None)
t = data[0]
y = data[1]
plt.plot(t,y)



ax1 = fig.add_subplot(ax[1])
ax1.axis('off')

Leg1()
Leg2()
plt.tight_layout()
plt.savefig("vpd_comparison_p.png")