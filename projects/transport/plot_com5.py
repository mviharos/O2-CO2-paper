import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Bathsheba_CO2_pul']
models = 'arterial'

elements = ['A1','A8']

#elements = ["R_pa"]
#models = 'heart_kim'
#elements = ['aorta','left-ventricular']

mmHg_to_Pa = 133.3616

start = 1

plt.figure()

data = pd.read_csv(os.path.join("results",  cases[0], models, elements[0] + ".txt"),header=None)
t = data[0]
p = (data[2-start]-1e5)/mmHg_to_Pa;
q=data[1]#*60000


plt.plot(t,q)

data = pd.read_csv(os.path.join("results",  cases[0], models, elements[1] + ".txt"),header=None)
t = data[0]
p = (data[2-start]-1e5)/mmHg_to_Pa;
q=data[1]

plt.plot(t,q)

plt.xlabel('time [s]')

#plt.ylabel('pressure [mmHg]')
#plt.ylabel('vfr [m3/s]')
plt.ylabel('vfr [l/min]')
leg = [" Lung " ,  " Left atrium " ]
#plt.legend(leg)
plt.grid()
plt.savefig('pic_q.png', bbox_inches="tight")

