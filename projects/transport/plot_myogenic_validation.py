import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#cases = ['Abel_ref3_myogenic_EBase','Abel_ref3_myogenic_Test_08','Abel_ref3_myogenic_Test_08_noMyo','Abel_ref3_myogenic_Test_07','Abel_ref3_myogenic_Test_07_noMyo'
#		,'Abel_ref3_myogenic_Test_09','Abel_ref3_myogenic_Test_09_noMyo']


"""
cases_Myo = ['Abel_ref3_myogenic_Test_05','Abel_ref3_myogenic_Test_08','Abel_ref3_myogenic_Test_09',
'Abel_ref3_myogenic_Base','Abel_ref3_myogenic_Test_11',
'Abel_ref3_myogenic_Test_12','Abel_ref3_myogenic_Test_14',
'Abel_ref3_myogenic_Test_18','Abel_ref3_myogenic_Test_25']

cases_noMyo = ['Abel_ref3_myogenic_Test_05NoMy','Abel_ref3_myogenic_Test_08NoMy',
'Abel_ref3_myogenic_Test_09NoMy','Abel_ref3_myogenic_Base',
'Abel_ref3_myogenic_Test_11NoMy','Abel_ref3_myogenic_Test_12NoMy',
'Abel_ref3_myogenic_Test_14NoMy','Abel_ref3_myogenic_Test_18NoMy',
'Abel_ref3_myogenic_Test_25NoMy']"""

cases_Myo = ['M1','M1_05','M1_1','M1_15','M1_2','M1_25','M0_95','M0_9','M0_85','M0_8','M0_75']

cases_noMyo = ['N1','N1_05','N1_1','N1_15','N1_2','N1_25','N0_95','N0_9','N0_85','N0_8','N0_75']

edges = ["A20","A5","A6","A15"]

def closest(lst, K):
     
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

    
def calcQ(model):
    p_min = 0
    p_max = 0
    q_sum = 0

    
    for j in range(len(edges)):
        data = np.genfromtxt(os.path.join("results", model , "arterial", edges[j] + ".txt"), delimiter=', ')
        dataT = data.T
        time = closest(list(dataT[0]),dataT[0][len(dataT[0])-1]-0.794)
        utolso_ciklus_index=list(dataT[0]).index(time)
        q = dataT[5][utolso_ciklus_index:]
        t = dataT[0][utolso_ciklus_index:]
        p = dataT[1][utolso_ciklus_index:]-1e5
        p_min = min(p)
        p_max = max(p)

        QQ = 0
        for Qindex in range(len(q)-1):
            QQ += (q[Qindex] + q[Qindex + 1]) * 0.5 * (t[Qindex+1] - t[Qindex])
        QQ = QQ/0.794*60*1e+06

        q_sum += QQ

    
    return [q_sum,  p_min, p_max]



mmHg_to_Pa = 133.3616

start = 1

plt.figure()

q = []
sys = []
dia = []
M = []

for i in range(len(cases_Myo)):
    vvv = calcQ(cases_Myo[i])
    q.append(vvv[0])
    dia.append(vvv[1]/mmHg_to_Pa)
    sys.append(vvv[2]/mmHg_to_Pa)
    M.append(vvv[0]/mmHg_to_Pa)


MAP = (np.array(sys) + np.array(dia) * 2) / 3
print(M)

#plt.scatter(MAP , q , color = 'darkblue', marker="x",s = 30)
#plt.plot(MAP , q , color = 'blue',linewidth = 2)

F = np.poly1d( np.polyfit(MAP, q, 3) )
t = np.linspace(75, 110, 250)
#mp.plot(p, q, 'o', t, F(t), '-', color='red')


# Plotting the data points and the fitted curve
plt.plot(t, F(t), color='lightcoral', label='Myogenic on fitted', linewidth=3, zorder=1)  # Fitted curve in red
plt.scatter(MAP, q, color='darkred', label='Myogenic on data points', s=60, zorder=3)  # Data points in blue


print(q)
q = []
sys = []
dia = []
M = []

for i in range(len(cases_noMyo)):
    vvv = calcQ(cases_noMyo[i])
    q.append(vvv[0])
    dia.append(vvv[1]/mmHg_to_Pa)
    sys.append(vvv[2]/mmHg_to_Pa)
    M.append(vvv[0]/mmHg_to_Pa)


MAP = (np.array(sys) + np.array(dia) * 2) / 3

F = np.poly1d( np.polyfit(MAP, q, 3) )

#plt.scatter(MAP , q , color = 'red',marker='x',s=30)
#plt.plot(MAP , q , color = 'pink',linewidth = 2)
plt.plot(t, F(t), color='lightsteelblue', label='Myogenic off fitted', linewidth=3, zorder=2)  # Fitted curve in red
plt.scatter(MAP, q, color='navy',marker='x', label='Myogenic off data points', s=60, zorder=4)  # Data points in blue

#plt.xlabel('MAP [mmHg]')
#plt.ylabel('CBF [%]')

plt.xlabel('Artériás közép nyomás [mmHg]')
plt.ylabel(r'Agyi véráramlás $[\frac{ml}{min} ]$')

#p1 = mpatches.Patch(color='darkblue', label='Myogenic on')
#p2 = mpatches.Patch(color='pink', label='Myogenic off')

p1 = mpatches.Patch(color='lightcoral', label='Aktív m. v. illesztett')
p2 = mpatches.Patch(color='darkred', label='Aktív m. v. adat pont')
p3 = mpatches.Patch(color='lightsteelblue', label='Inaktív m. v. illesztett')
p4 = mpatches.Patch(color='navy', label='Inaktív m. v. adat pont')
plt.legend(ncol=1,handles=[p1,p2,p3,p4], loc='upper left')



plt.grid()
plt.savefig('compare.png')

