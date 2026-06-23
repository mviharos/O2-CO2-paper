import matplotlib.pyplot as plt
import pandas as pd
import os

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q


compartments = ['pul_art','pul_cap','pul_vein']


def abrazol0D(i, cstart, cend):
    data = pd.read_csv(os.path.join("results",'Bathsheba', "heart_kim_lit", "C_Plasma_O2", compartments[i] + ".txt"),header=None)
    t = data[0]
    RBCs = data[1]
    RBCe = data[2]
    plt.plot(t,RBCs, color = cstart)
    plt.plot(t,RBCe, color = cend)

def abrazol0D_0D(i, cstart):
    data = pd.read_csv(os.path.join("results",'Bathsheba', "heart_kim_lit", "C_Plasma_O2", compartments[i] + ".txt"),header=None)
    t = data[0]
    RBC = data[1]
    plt.plot(t,RBC, color = cstart)



fig, ax = plt.subplots(3, 1, figsize=(8,8))
fig.tight_layout(pad=1.4)

"""
ax1 = fig.add_subplot(ax[0])
abrazol0D_0D(0,'red')
leg = ['Right atrium']
plt.grid()
plt.legend(leg)
plt.ylabel('O2 concentration [m3/m3]')
plt.xlabel('time [s]')

ax1 = fig.add_subplot(ax[1])
abrazol0D_0D(1,'red')
leg = ['Right ventricle']
plt.grid()
plt.legend(leg)
plt.ylabel('O2 concentration [m3/m3]')
plt.xlabel('time [s]')"""

ax1 = fig.add_subplot(ax[0])
abrazol0D(0,'darkorange','darkmagenta')
leg = ['Pulmonary artery s.','Pulmonary artery e.']
plt.grid()
plt.legend(leg)
plt.ylabel('O2 concentration [m3/m3]')
plt.xlabel('time [s]')

ax1 = fig.add_subplot(ax[1])
abrazol0D(1,'darkorange','darkmagenta')
leg = ['Pulmonary capillary s.','Pulmonary capillary e.']
plt.grid()
plt.legend(leg)
plt.ylabel('O2 concentration [m3/m3]')
plt.xlabel('time [s]')

ax1 = fig.add_subplot(ax[2])
abrazol0D(2,'darkorange','darkmagenta')
leg = ['Pulmonary vein s.','Pulmonary vein e.']
plt.grid()
plt.legend(leg)
plt.ylabel('O2 concentration [m3/m3]')
plt.xlabel('time [s]')

"""
ax1 = fig.add_subplot(ax[5])
abrazol0D_0D(5,'red')
leg = ['Left atrium']
plt.grid()
plt.legend(leg)
plt.ylabel('O2 concentration [m3/m3]')
plt.xlabel('time [s]')

ax1 = fig.add_subplot(ax[6])
abrazol0D_0D(6,'red')
leg = ['Left ventricle']
plt.grid()
plt.legend(leg)
plt.ylabel('O2 concentration [m3/m3]')
plt.xlabel('time [s]')"""


plt.tight_layout()
plt.savefig("C_Plasma_O2_heart.jpg", dpi=150)

