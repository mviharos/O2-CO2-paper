import matplotlib.pyplot as plt
import pandas as pd
import os

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Bathsheba']
models = ['p10']

compartments = ['arteriole','capillary','venulare','vein']

stuff=['CO2_pla','CO2_rbc','HCO3_rbc','HCO3_pla','HbCO2']



def abrazol(i, cstart, cend):
    data = pd.read_csv(os.path.join("results",'Bathsheba', "p10", stuff[i], "capillary.txt"),header=None)
    t = data[0]
    RBCs = data[1]
    RBCe = data[2]
    plt.plot(t,RBCs, color = cstart,linestyle='dashed')
    plt.plot(t,RBCe, color = cend,linestyle='dashed')


fig, ax = plt.subplots(5, 1, figsize=(12,8))
fig.tight_layout(pad=1.4)
ax1 = fig.add_subplot(ax[0])
abrazol(0, 'pink', 'deeppink')
plt.ylabel('co2_pla [m3/m3]')
leg = ['s.','e.']
plt.grid()
plt.legend(leg)

ax1 = fig.add_subplot(ax[1])
abrazol(1, 'pink', 'deeppink')
plt.ylabel('co2_rbc [m3/m3]')
leg = ['s.','e.']
plt.grid()
plt.legend(leg)

ax1 = fig.add_subplot(ax[2])
abrazol(2, 'pink', 'deeppink')
plt.ylabel('hco3_rbc [m3/m3]')
leg = ['s.','e.']
plt.grid()
plt.legend(leg)

ax1 = fig.add_subplot(ax[3])
abrazol(3, 'pink', 'deeppink')
plt.ylabel('hco3_pla [m3/m3]')
leg = ['s.','e.']
plt.grid()
plt.legend(leg)

ax1 = fig.add_subplot(ax[4])
abrazol(4, 'pink', 'deeppink')
plt.ylabel('hbco2 [m3/m3]')
leg = ['s.','e.']
plt.grid()
plt.legend(leg)
"""
plt.ylabel('c [?]')
leg = ['Aorta s.','Aorta e.',
       'I. Carotid s.','I. Carotid e.',
       'A. Tribial s.','A. Tribial e.',
       'Radial s.','Radial e.']
plt.grid()
plt.legend(leg)


ax1 = fig.add_subplot(ax[1])
abrazol0D(0,'darkorange','darkmagenta')
leg = ['s.','e.']
plt.grid()
plt.legend(leg)
plt.ylabel('c [cell/m3]')
"""

plt.tight_layout()
plt.savefig("CO2.jpg", dpi=150)

