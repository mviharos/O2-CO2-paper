import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Abel_ref3_myogenic_Base_NoMy','Abel_ref3_myogenic_Base_My','Abel_ref3_myogenic_mod_My','Abel_ref3_myogenic_mod_NoMy']
models = 'p43'
elements = ['Q1','Q1']

#models = 'heart_kim'
#elements = ['aorta','left-ventricular']

mmHg_to_Pa = 133.3616

start = 1

plt.figure()
data = pd.read_csv(os.path.join("results",  cases[0], models, elements[0] + ".txt"),header=None)
t = data[0]
p = (data[2-start]-1e5)/mmHg_to_Pa;

plt.plot(t,p,color='red')


data = pd.read_csv(os.path.join("results",  cases[1], models, elements[0] + ".txt"),header=None)
t = data[0]
p = (data[2-start]-1e5)/mmHg_to_Pa;

plt.plot(t,p,color='black')

data = pd.read_csv(os.path.join("results",  cases[2], models, elements[0] + ".txt"),header=None)
t = data[0]
p = (data[2-start]-1e5)/mmHg_to_Pa;

plt.plot(t,p,color='yellow')

data = pd.read_csv(os.path.join("results",  cases[3], models, elements[0] + ".txt"),header=None)
t = data[0]
p = (data[2-start]-1e5)/mmHg_to_Pa;

plt.plot(t,p,color='blue')



plt.xlabel('time [s]')
#plt.ylabel('volume flow rate [ml/s]')
plt.ylabel('pressure [mmHg]')
leg = ['Abel_ref3_myogenic_Base_NoMy','Abel_ref3_myogenic_Base_My','Abel_ref3_myogenic_mod_My','Abel_ref3_myogenic_mod_NoMy']
plt.legend(leg)
plt.grid()
plt.savefig('compare.png')

