import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

#models = 'heart_kim'
#elements = ['aorta','left-ventricular']

mmHg_to_Pa = 133.3616

start = 1

plt.figure()
data = pd.read_csv(os.path.join("results//Bathsheba_metOf_exOf//p10//tissueO2.txt"),header=None)
t = data[0]
tiss = data[1]
plt.plot(t,tiss, color='lightsteelblue', linestyle = '--', linewidth = 2.5)


data = pd.read_csv(os.path.join("results//Bathsheba_metOn_exOf//p10//tissueO2.txt"),header=None)
t = data[0]
tiss = data[1]
plt.plot(t,tiss, color='navy', linewidth = 2.5)


data = pd.read_csv(os.path.join("results//Bathsheba_metOf_exOn//p10//tissueO2.txt"),header=None)
t = data[0]
tiss = data[1]
plt.plot(t,tiss, color='lightcoral', linestyle = '--',linewidth = 2.5)


data = pd.read_csv(os.path.join("results//Bathsheba_metOn_exOn//p10//tissueO2.txt"),header=None)
t = data[0]
tiss = data[1]
plt.plot(t,tiss, color='darkred', linewidth = 2.5)


leg = [r'Névleges $O_2$ f., inaktív m. v.',r'Névleges $O_2$ f., aktív m. v.','Emelt $O_2$ f., inaktív m. v.', 'Emelt $O_2$ f., aktív m. v.']
#leg = ['Exercise off, metabolic off','Exercise off, metabolic on','Exercise on, metabolic off', 'Exercise on, metabolic on']
plt.grid()
plt.legend(leg)

plt.xlabel('Idő [s]')
plt.ylabel(r'Szövet $O_2$ koncentráció $[\frac{m^3}{m^3}]$')
plt.tight_layout()

plt.savefig('tissueO2.png')

