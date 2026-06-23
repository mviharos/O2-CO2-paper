import matplotlib.pyplot as plt
import pandas as pd
import os

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

models = ['arterial','arterial','arterial','arterial','venous','venous','venous']

elements = ['A1','A12','A55','A8',
            "189","215","84"]
compartments = ['arteriole','capillary','venulare']


def abrazol(i, cstart, cend):
    data = pd.read_csv(os.path.join("results",'Bathsheba_CO2_pul', models[i] , elements[i] + ".txt"),header=None)
    t = data[0]
    RBCs = data[19]
    RBCe = data[20]
    plt.plot(t,RBCs, color = cstart)
    plt.plot(t,RBCe, color = cend)


def abrazol0D(i, cstart, cend):
    data = pd.read_csv(os.path.join("results",'Bathsheba_CO2_pul', "p10", "CO2_pla", compartments[i] + ".txt"),header=None)
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
abrazol(4, 'pink', 'deeppink')
abrazol(5, 'yellow', 'goldenrod')
abrazol(6, 'lightblue', 'blue')
plt.ylabel('HB saturation [1]')
leg = ['R.ulnarv. s.',"R.ulnarv. e.",
        'L.ant.tibialv. s.','L.ant.tibialv. e.',
        'Sup.venacava s.','Sup.venacava e.']
plt.grid()
plt.legend(leg)



plt.tight_layout()
plt.savefig("CO2pla_full.jpg", dpi=150)

