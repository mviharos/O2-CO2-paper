import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Abel_ref3_myogenic_RBC', 'Abel_ref3_myogenic_RBC']
models = 'arterial'
elements = ['A1','A1']

mmHg_to_Pa = 133.3616

start = 1

plt.figure()
data = pd.read_csv(os.path.join("results",cases[0], models, elements[0] + ".txt"),header=None)
t = data[0]
p = (data[2-start]-1e5)/mmHg_to_Pa;
#q = data[6-start]*1e6*60;
#v = data[4-start];
#a = data[16-start];
#p = (data[1]-1e5)/mmHg_to_Pa;

t1=list(t)
p1=list(p)
hossz=len(t1)
mennyit=round(hossz/26)
print(hossz,mennyit)
plt.figure(figsize=(12,6))

plt.plot(np.array(t1[(hossz-mennyit):(hossz-1)])-t1[(hossz-mennyit)],p1[(hossz-mennyit):(hossz-1)],color='orangered',linewidth=3)

start = 1
"""
data = pd.read_csv(os.path.join("results",cases[1], models, elements[1] + ".txt"),header=None)
t = data[0]
p = (data[2-start]-1e5)/mmHg_to_Pa;
q = data[6-start]*1e6*60;
#v = data[4-start];
#a = data[16-start];
#p = (data[1]-1e5)/mmHg_to_Pa;
#q = data[2]*1e6



#plt.plot(t,p)

plt.xlabel('time [s]')
#plt.ylabel('volume flow rate [ml/s]')
plt.ylabel('Aortic pressure [mmHg]')
leg = [elements[0] + " - " + cases[0],elements[1] + " - " + cases[1]]
#plt.legend(leg)
plt.grid()"""

plt.xlabel("time [s]")
plt.ylabel('Pressure [mmHg]')
plt.grid()
plt.savefig(elements[0]+'.png')

