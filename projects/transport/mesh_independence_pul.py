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


def Leg():
    m0 = mpatches.Patch(color='darkslategrey', label='Pulmonary capillary plasma oxygen concentration data points')
    m1 = mpatches.Patch(color='teal', label='Pulmonary capillary plasma oxygen concentration fitted')
    m2 = mpatches.Patch(color='indianred', label='Pulmonary capillary HB saturation fitted')
    m3 = mpatches.Patch(color='maroon', label='Pulmonary capillary HB saturation data points')
    plt.legend(ncol=1,handles=[m0,m1,m3,m2],bbox_to_anchor=(0.3, 0.87), loc='center',fontsize=10)

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


def abrazol(cpo2,hbo2, title):
    x=[0.5,1,2,4,8]
    xx = np.linspace(0.3, 9, 60)

    popt, pcov = curve_fit(func, x, cpo2,p0=(-0.02320328 , 1.52448446 , 1.01089422),maxfev=10000)
    yy = func(xx, *popt)
    plt.plot(xx, yy,color='teal',linewidth=2.5)

    plt.scatter(x, cpo2,color='darkslategrey',s=50)


    popt, pcov = curve_fit(func, x, hbo2,p0=(-0.02320328 , 1.52448446 , 1.01089422),maxfev=10000)
    yy = func(xx, *popt)
    plt.plot(xx, yy,color='indianred',linewidth=2.5)

    plt.scatter(x, hbo2,color='maroon',s=50)
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


names=['Abel_ref3_myogenic_RBC_O2_05','Abel_ref3_myogenic_RBC_O2_1','Abel_ref3_myogenic_RBC_O2_2','Abel_ref3_myogenic_RBC_O2_4','Abel_ref3_myogenic_RBC_O2_8']

T = 75.

ax1 = fig.add_subplot(ax[0])
cpo2 = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results_pul",names[i], "heart_kim_lit", "C_Plasma_O2", "pul_cap.txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[2]
    time = closest(t,T)
    index=list(t).index(time)
    cpo2[i] = co[index]

hbo2 = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results_pul",names[i], "heart_kim_lit", "HB_O2", "pul_cap.txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[2]
    time = closest(t,T)
    index=list(t).index(time)
    hbo2[i] = co[index]

for i in range(5):
    cpo2[4-i]/=cpo2[0]
    hbo2[4-i]/=hbo2[0]


abrazol(cpo2,hbo2, 'Oxgen uptake model mesh independence')
ax1 = fig.add_subplot(ax[1])
ax1.axis('off')

Leg()
plt.tight_layout()
plt.savefig("mesh_indep_perif_pul.png")