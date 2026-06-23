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
data = pd.read_csv(os.path.join("results//Abel_ref3_myogenic_RBC_O2_base//p10//HB_O2//capillary.txt"),header=None)
t = data[0]
tiss = data[2]
plt.plot(t,tiss, color='blue')


data = pd.read_csv(os.path.join("results//Abel_ref3_myogenic_RBC_O2_ex_on//p10//HB_O2//capillary.txt"),header=None)
t = data[0]
tiss = data[2]
plt.plot(t,tiss, color='red')


data = pd.read_csv(os.path.join("results//Abel_ref3_myogenic_RBC_O2_ex_off//p10//HB_O2//capillary.txt"),header=None)
t = data[0]
tiss = data[2]
plt.plot(t,tiss, color='purple')

leg = ['base','exercise, metabolic on', 'exercise, metabolic off']
plt.grid()
plt.legend(leg)

plt.xlabel('time [s]')
#plt.ylabel('volume flow rate [ml/s]')
plt.ylabel('HB saturation [1]')
#leg = ["Base_NoMy." , "mod_My"]
#plt.legend(leg)
plt.tight_layout()
plt.savefig('HB_sat' + '.png')

