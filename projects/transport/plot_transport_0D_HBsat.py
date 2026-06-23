import matplotlib.pyplot as plt
import pandas as pd
import os

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Abel_ref3_myogenic_RBC_O2','Abel_ref3_myogenic_RBC_O2','Abel_ref3_myogenic_RBC_O2','Abel_ref3_myogenic_RBC_O2']
models = ['arterial','arterial','arterial','arterial']

elements = ['A1','A12','A55','A8']
compartments = ['arteriole','capillary','venulare','vein']


def abrazol(i, cstart, cend):
    data = pd.read_csv(os.path.join("results",cases[i], models[i] , elements[i] + ".txt"),header=None)
    t = data[0]
    RBCs = data[15]
    RBCe = data[16]
    plt.plot(t,RBCs, color = cstart)
    plt.plot(t,RBCe, color = cend)


def abrazol0D(i, cstart, cend):
    data = pd.read_csv(os.path.join("results",'Abel_ref3_myogenic_RBC_O2', "p10", "HB_O2", compartments[i] + ".txt"),header=None)
    t = data[0]
    RBCs = data[1]
    RBCe = data[2]
    plt.plot(t,RBCs, color = cstart,linestyle='dashed')
    plt.plot(t,RBCe, color = cend,linestyle='dashed')


fig, ax = plt.subplots(5, 1, figsize=(8,12))
fig.tight_layout(pad=1.4)
ax1 = fig.add_subplot(ax[0])

abrazol(0, 'pink', 'deeppink')
abrazol(1, 'yellow', 'goldenrod')
abrazol(2, 'lightblue', 'blue')
abrazol(3, 'olivedrab', 'darkgreen')
plt.ylabel('HB saturation [1]')
leg = ['Aorta s.','Aorta e.',
       'I. Carotid s.','I. Carotid e.',
       'A. Tribial s.','A. Tribial e.',
       'Radial s.','Radial e.']
plt.grid()
plt.legend(leg)


ax1 = fig.add_subplot(ax[1])
abrazol0D(0,'darkorange','darkmagenta')
leg = ['Arteriole s.','Arteriole e.']
plt.grid()
plt.legend(leg)
plt.ylabel('HB saturation [1]')


ax1 = fig.add_subplot(ax[2])
abrazol0D(1,'darkorange','darkmagenta')
leg = ['Capillary s.','Capillary e.']
plt.grid()
plt.legend(leg)
plt.ylabel('HB saturation [1]')

ax1 = fig.add_subplot(ax[3])
abrazol0D(2,'darkorange','darkmagenta')
leg = ['Venulare s.','Venulare e.']
plt.grid()
plt.legend(leg)
plt.ylabel('HB saturation [1]')

ax1 = fig.add_subplot(ax[4])
abrazol0D(3,'darkorange','darkmagenta')
leg = ['Vein s.','Vein e.']
plt.grid()
plt.legend(leg)
plt.ylabel('HB saturation [1]')
plt.xlabel('time [s]')

plt.tight_layout()
plt.savefig("HBsat.jpg", dpi=150)

