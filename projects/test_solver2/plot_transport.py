import matplotlib.pyplot as plt
import pandas as pd
import os

# Halasz_P045_resistance
# Reymond_103
# Reymond_103_Q

cases = ['Abel_ref3_myogenic_RBC','Abel_ref3_myogenic_RBC','Abel_ref3_myogenic_RBC','Abel_ref3_myogenic_RBC']
models = ['arterial','arterial','arterial','arterial']

elements = ['A1','A12','A55','A8']


def abrazol(i, cstart, cend):
    data = pd.read_csv(os.path.join("results",cases[i], models[i] , elements[i] + ".txt"),header=None)
    t = data[0]
    RBCs = data[13]
    RBCe = data[14]
    plt.plot(t,RBCs, color = cstart)
    plt.plot(t,RBCe, color = cend)



abrazol(0, 'pink', 'deeppink')
abrazol(1, 'yellow', 'goldenrod')
abrazol(2, 'lightblue', 'blue')
abrazol(3, 'olivedrab', 'darkgreen')


plt.xlabel('time [s]')
plt.ylabel('magic [-]')
leg = ['Aorta s.','Aorta e.',
       'I. Carotid s.','I. Carotid e.',
       'A. Tribial s.','A. Tribial e.',
       'Radial s.','Radial e.']


plt.legend(leg)
plt.grid()
plt.savefig("transport_test_rainbow.jpg", dpi=150)

