import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

#cases = ['Abel_ref3_myogenic_RBC_O2']
elements = ['p8']

#models = 'heart_kim'
#elements = ['aorta','left-ventricular']

mmHg_to_Pa = 133.3616

start = 1

plt.figure()
#data = pd.read_csv(os.path.join("results//Erik//p10//tissueO2.txt"),header=None)
data = pd.read_csv(os.path.join("results//Bathsheba//arterial//A1.txt"),header=None)
t = data[0]
tiss = (data[1]-1e5)/133.3
plt.plot(t,tiss)


plt.xlabel('time [s]')
#plt.ylabel('volume flow rate [ml/s]')
plt.ylabel('Tissue O2 [m3/m3]')
#leg = ["Base_NoMy." , "mod_My"]
#plt.legend(leg)
plt.grid()
plt.tight_layout()
plt.savefig('test.png')

