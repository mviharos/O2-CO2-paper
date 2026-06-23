import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.pyplot as mp


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
'Abel_ref3_myogenic_Test_25NoMy']
"""

#cases_Myo = ["Abel_ref3_myogenic_B","Abel_ref3_myogenic_E1","Abel_ref3_myogenic_E12","Abel_ref3_myogenic_E4","Abel_ref3_myogenic_E16","Abel_ref3_myogenic_E20","Abel_ref3_myogenic_E2","Abel_ref3_myogenic_E9","Abel_ref3_myogenic_E6"]

#cases_noMyo = ["Abel_ref3_myogenic_BN","Abel_ref3_myogenic_E1N","Abel_ref3_myogenic_E12N","Abel_ref3_myogenic_E4N","Abel_ref3_myogenic_E16N","Abel_ref3_myogenic_E20N","Abel_ref3_myogenic_E2N","Abel_ref3_myogenic_E9N","Abel_ref3_myogenic_E6N"]

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
    return q_sum

def calcA1Q(model):

    data = np.genfromtxt(os.path.join("results", model , "arterial", "A1.txt"), delimiter=', ')
    dataT = data.T
    time = closest(list(dataT[0]),dataT[0][len(dataT[0])-1]-0.794)
    utolso_ciklus_index=list(dataT[0]).index(time)
    q = dataT[5][utolso_ciklus_index:]
    t = dataT[0][utolso_ciklus_index:]
    QQ = 0
    for Qindex in range(len(q)-1):
        QQ += (q[Qindex] + q[Qindex + 1]) * 0.5 * (t[Qindex+1] - t[Qindex])
    QQ = QQ/0.794*60*1e+06

    return QQ

def Pavg(model):

    for j in range(len(edges)):
        data = np.genfromtxt(os.path.join("results", model , "arterial", "A1" + ".txt"), delimiter=', ')
        dataT = data.T
        time = closest(list(dataT[0]),dataT[0][len(dataT[0])-1]-0.794)
        utolso_ciklus_index=list(dataT[0]).index(time)
        q = dataT[5][utolso_ciklus_index:]
        t = dataT[0][utolso_ciklus_index:]
        p = dataT[1][utolso_ciklus_index:]-1e5

        PP = 0
        for Qindex in range(len(q)-1):
            PP += (p[Qindex] + p[Qindex + 1]) * 0.5 * (t[Qindex+1] - t[Qindex])

    return PP/0.794

mmHg_to_Pa = 133.3616

start = 1

plt.figure()

q = []
p = []


for i in range(len(cases_Myo)):
    vvv = calcQ(cases_Myo[i])
    q.append(vvv/896*100)
    p.append(Pavg(cases_Myo[i])/mmHg_to_Pa)



F = np.poly1d( np.polyfit(p, q, 3) )
t = np.linspace(65, 110, 250)
#mp.plot(p, q, 'o', t, F(t), '-', color='red')


# Plotting the data points and the fitted curve
plt.plot(t, F(t), color='lightcoral', label='Myogenic on fitted', linewidth=3, zorder=1)  # Fitted curve in red
plt.scatter(p, q, color='darkred', label='Myogenic on data points', s=60, zorder=3)  # Data points in blue

q = []
p = []


for i in range(len(cases_noMyo)):
    vvv = calcQ(cases_noMyo[i])
    q.append(vvv/896*100)
    p.append(Pavg(cases_noMyo[i])/mmHg_to_Pa)


#poly
F = np.poly1d( np.polyfit(p, q, 3) )
t = np.linspace(65, 110, 250)
#mp.plot(p, q, 'o',  t, F(t), '-', color='indigo')
plt.plot(t, F(t), color='lightsteelblue', label='Myogenic off fitted', linewidth=3, zorder=2)  # Fitted curve in red
plt.scatter(p, q, color='navy',marker='x', label='Myogenic off data points', s=60, zorder=4)  # Data points in blue


plt.xlabel('MAP [mmHg]')
plt.ylabel('CBF [%]')
plt.ylim((50,150))

#p1 = mpatches.Patch(color='orange', label='Myogenic on fitted')
#p2 = mpatches.Patch(color='red', label='Myogenic off fitted')
#p3 = mpatches.Patch(color='blue', label='Myogenic on data points')
#p4 = mpatches.Patch(color='green', label='Myogenic off data points')


#plt.legend(ncol=1,handles=[p1,p2,p3,p4], loc='upper left')

plt.legend()
plt.grid()


#plt.scatter(Pavg('Abel_ref3_myogenic')/mmHg_to_Pa,calcQ('Abel_ref3_myogenic')/877,color="black")

plt.savefig('compare.png')

