import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Abel_ref3_myogenic_RBC_O2']
elements = ['p8']

#models = 'heart_kim'
#elements = ['aorta','left-ventricular']

mmHg_to_Pa = 133.3616

start = 1

plt.figure()
data = pd.read_csv(os.path.join("results//Abel_ref3_myogenic_RBC_O2_exof_of//p10//tissueO2.txt"),header=None)
t = data[0]
tiss = data[1]
plt.plot(t,tiss, color='lightsteelblue', linestyle = '--', linewidth = 2.5)


data = pd.read_csv(os.path.join("results//Abel_ref3_myogenic_RBC_O2_exof_on//p10//tissueO2.txt"),header=None)
t = data[0]
tiss = data[1]
plt.plot(t,tiss, color='navy', linewidth = 2.5)


data = pd.read_csv(os.path.join("results//Abel_ref3_myogenic_RBC_O2_exon_off//p10//tissueO2.txt"),header=None)
t = data[0]
tiss = data[1]
plt.plot(t,tiss, color='lightcoral', linestyle = '--',linewidth = 2.5)


data = pd.read_csv(os.path.join("results//Abel_ref3_myogenic_RBC_O2_exon_on//p10//tissueO2.txt"),header=None)
t = data[0]
tiss = data[1]
plt.plot(t,tiss, color='darkred', linewidth = 2.5)


leg = ['Exercise off, metabolic off','Exercise off, metabolic on','Exercise on, metabolic off', 'Exercise on, metabolic on']
plt.grid()
plt.legend(leg)

plt.xlabel('time [s]')
plt.ylabel('Tissue O2 concentration [m3/m3]')
plt.tight_layout()
plt.savefig('tissueO2.png')

