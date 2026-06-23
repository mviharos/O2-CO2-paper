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
    m0 = mpatches.Patch(color='grey', label='Arterioles s. fitted')
    m1 = mpatches.Patch(color='black', label='Arterioles s. data pints')

    m2 = mpatches.Patch(color='orangered', label='Capillaries s. fitted')
    m3 = mpatches.Patch(color='darkred', label='Capillaries s. data points')

    m4 = mpatches.Patch(color='darkblue', label='Venulares s. fitted')
    m5 = mpatches.Patch(color='navy', label='Venulares s. data points')

    m6 = mpatches.Patch(color='mediumvioletred', label='Veins s. fitted')
    m7 = mpatches.Patch(color='purple', label='Veins s. data points')

    m8 = mpatches.Patch(color='lightpink', label='Tissue fitted')
    m9 = mpatches.Patch(color='darkred', label='Tissue data points')
    plt.legend(ncol=1,handles=[m0,m1,m2,m3,m4,m5,m6,m7,m8,m9],bbox_to_anchor=(0.3, 0.6), loc='center',fontsize=10)

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


def abrazol(a,c,ven,vei, title):
    x=[0.5,1,2,4,8]
    xx = np.linspace(0.3, 9, 60)


    popt, pcov = curve_fit(func, x, a,p0=(-0.02320328 ,1.52448446 , 1.01089422),maxfev=10000)
    yy = func(xx, *popt)
    plt.plot(xx, yy,color='gray',linewidth=2.5)
    #print(popt)


    popt, pcov = curve_fit(func, x, c,p0=(-0.02320328 , 1.52448446 , 1.01089422),maxfev=10000)
    yy = func(xx, *popt)
    plt.plot(xx, yy,color='orangered',linewidth=2.5)    


    popt, pcov = curve_fit(func, x, ven,p0=(-0.02320328 , 1.52448446 , 1.01089422),maxfev=10000)
    yy = func(xx, *popt)
    plt.plot(xx, yy,color='darkblue',linewidth=2.5)


    popt, pcov = curve_fit(func, x, vei,p0=(-0.02320328 , 1.52448446 , 1.01089422),maxfev=10000)
    yy = func(xx, *popt)
    plt.plot(xx, yy,color='mediumvioletred',linewidth=2.5)


    plt.scatter(x, a,color='black',s=50)
    plt.scatter(x, c,color='darkred',s=50)
    plt.scatter(x, ven,color='navy',s=50)
    plt.scatter(x, vei,color='purple',s=50)
    plt.grid()

    plt.xlabel("Multiplicator of nominal graid points [1]")
    plt.title(title,fontsize=13)
    plt.ylabel("Normalised transport variable [1]")

def abrazol2(tissue, title):
    x=[0.5,1,2,4,8]
    xx = np.linspace(0.3, 9, 60)   

    popt, pcov = curve_fit(func, x, tissue,p0=(-0.02320328 , 1.52448446 , 1.01089422),maxfev=10000)
    yy = func(xx, *popt)
    plt.plot(xx, yy,color='lightpink',linewidth=2.5)
    plt.scatter(x, tissue,color='darkred',s=50)
    plt.grid()

    plt.xlabel("Multiplicator of nominal grid points [1]")
    plt.title(title,fontsize=13)
    plt.ylabel("Normalised transport variable [1]")



def PaTommHg(L):
    for i in range(len(L)):
        L[i]=(L[i]-1e5)/133.3
    return L


fig, ax = plt.subplots(2, 2, figsize=(10,7))
fig.tight_layout(pad=1.)
plt.subplots_adjust(left=0.1,
                    bottom=0.05,
                    right=0.92,
                    top=0.95,
                    wspace=0.3,
                    hspace=0.35)

#p0

names=['Abel_ref3_myogenic_RBC_O2_05','Abel_ref3_myogenic_RBC_O2_1','Abel_ref3_myogenic_RBC_O2_2','Abel_ref3_myogenic_RBC_O2_4','Abel_ref3_myogenic_RBC_O2_8']

a_t = 20.
c_t = 22.
ven_t = 5.
vei_t = 10.

a_t = 75.
c_t = 75.
ven_t = 75.
vei_t = 75.

ax1 = fig.add_subplot(ax[0, 0])
a = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "C_Plasma_O2", "arteriole" + ".txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,a_t)
    index=list(t).index(time)
    a[i] = co[index]

c = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "C_Plasma_O2", "capillary" + ".txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,c_t)
    index=list(t).index(time)
    c[i] = co[index]

ven = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "C_Plasma_O2", "venulare" + ".txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,ven_t)
    index=list(t).index(time)
    ven[i] = co[index]

vei = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "C_Plasma_O2", "vein" + ".txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,ven_t)
    index=list(t).index(time)
    vei[i] = co[index]

for i in range(5):
    a[4-i]/=a[0]
    c[4-i]/=c[0]
    vei[4-i]/=vei[0]
    ven[4-i]/=ven[0]

abrazol(a,c,ven,vei, 'Plasma oxygen concentration')


ax1 = fig.add_subplot(ax[0, 1])

a = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "HB_O2", "arteriole" + ".txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,a_t)
    index=list(t).index(time)
    a[i] = co[index]


#print(a)
c = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "HB_O2", "capillary" + ".txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,c_t)
    index=list(t).index(time)
    c[i] = co[index]

ven = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "HB_O2", "venulare" + ".txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,ven_t)
    index=list(t).index(time)
    ven[i] = co[index]

vei = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "HB_O2", "vein" + ".txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,ven_t)
    index=list(t).index(time)
    vei[i] = co[index]


for i in range(5):
    a[4-i]/=a[0]
    c[4-i]/=c[0]
    vei[4-i]/=vei[0]
    ven[4-i]/=ven[0]


abrazol(a,c,ven,vei, 'HB saturation')


ax1 = fig.add_subplot(ax[1, 0])
tiss = [0,0,0,0,0]
for i in range(len(names)):
    data = pd.read_csv(os.path.join("results",names[i], "p10", "tissueO2.txt"),header=None)
    dataT = data.T
    t = data[0]
    co = data[1]
    time = closest(t,75)
    index=list(t).index(time)
    tiss[i] = co[index]

for i in range(5):
    tiss[4-i]/=tiss[0]
abrazol2(tiss, 'Tissue oxygen concentration')

ax1 = fig.add_subplot(ax[1, 1])

ax1.axis('off')

Leg()
plt.tight_layout()
plt.savefig("mesh_indep_perif.png")