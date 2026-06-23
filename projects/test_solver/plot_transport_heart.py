import matplotlib.pyplot as plt
import pandas as pd
import os

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Abel_ref3_myogenic_RBC_O2',
         'Abel_ref3_myogenic_RBC_O2',
         'Abel_ref3_myogenic_RBC_O2',
         'Abel_ref3_myogenic_RBC_O2',
         'Abel_ref3_myogenic_RBC_O2',
         'Abel_ref3_myogenic_RBC_O2']


compartments = ['RA','RV','pul_art','pul_vein','LA','LV']


def abrazol0D(i, cstart, cend):
    data = pd.read_csv(os.path.join("results",'Abel_ref3_myogenic_RBC_O2', "heart_kim_lit", compartments[i] + ".txt"),header=None)
    t = data[0]
    RBCs = data[1]
    RBCe = data[2]
    plt.plot(t,RBCs, color = cstart)
    plt.plot(t,RBCe, color = cend)

def abrazol0D_0D(i, cstart):
    data = pd.read_csv(os.path.join("results",'Abel_ref3_myogenic_RBC_O2', "heart_kim_lit", compartments[i] + ".txt"),header=None)
    t = data[0]
    RBC = data[1]
    plt.plot(t,RBC, color = cstart)



fig, ax = plt.subplots(6, 1, figsize=(8,12))
fig.tight_layout(pad=1.4)

ax1 = fig.add_subplot(ax[0])
abrazol0D_0D(0,'red')
leg = ['RA']
plt.grid()
plt.legend(leg)
plt.ylabel('c [?]')
plt.xlabel('time [s]')

ax1 = fig.add_subplot(ax[1])
abrazol0D_0D(1,'red')
leg = ['RV']
plt.grid()
plt.legend(leg)
plt.ylabel('c [?]')
plt.xlabel('time [s]')

ax1 = fig.add_subplot(ax[2])
abrazol0D_0D(2,'darkorange')
leg = ['pul_art s.']
plt.grid()
plt.legend(leg)
plt.ylabel('c [?]')

ax1 = fig.add_subplot(ax[3])
abrazol0D(3,'darkorange','darkmagenta')
leg = ['pul_vein s.','pul_vein e.']
plt.grid()
plt.legend(leg)
plt.ylabel('c [?]')

ax1 = fig.add_subplot(ax[4])
abrazol0D_0D(4,'red')
leg = ['LA']
plt.grid()
plt.legend(leg)
plt.ylabel('c [?]')

ax1 = fig.add_subplot(ax[5])
abrazol0D_0D(5,'red')
leg = ['LV']
plt.grid()
plt.legend(leg)
plt.ylabel('c [?]')
plt.xlabel('time [s]')



plt.savefig("transport_test_heart.jpg", dpi=150)

