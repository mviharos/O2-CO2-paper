import matplotlib.pyplot as plt
import pandas as pd
import os

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Abel_ref2_vein_valve','Abel_ref2_vein_valve']
models = ['arterial','arterial']

elements = ['AA0','A8']


start=1
data = pd.read_csv(os.path.join("results" ,cases[0] , models[0] , elements[0] + ".txt"),header=None)
t = data[0]
#p = (data[2-start]-1e5)/mmHg_to_Pa;
vs = data[4-start];

plt.plot(t,vs)



data = pd.read_csv(os.path.join("results" ,cases[1] , models[1] , elements[1] + ".txt"),header=None)
t = data[0]
ve = data[5-start];
#plt.plot(t,ve)
#p = (data[2-start]-1e5)/mmHg_to_Pa;
#ve = data[5-start];


plt.xlabel('time [s]')
#plt.ylabel('volume flow rate [ml/s]')
plt.ylabel('v [m/s]')
leg = ['AA0start','A8end']
plt.legend(leg)
plt.grid()
#plt.show()
plt.savefig("valvetest.jpg")

# node plot
# plt.figure()
# model = "p1"
# node_id = "R1"
# data = pd.read_csv("results\\" + cases[1] + "\\" + model + "\\" + node_id + ".txt",header=None)
# t = data[0]
# #p = (data[1]-1e5)/mmHg_to_Pa;9
# q = data[1]*1e6
# plt.plot(t,q)
# plt.grid()
# plt.show()
