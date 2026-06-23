# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:32:15 2022

@author: Viharos
"""

import numpy as np
import pandas as pd
import os
from os.path import exists


def closest(lst, K):
     
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
        
def calcQ(Aindex, adatindex):

    #data = np.genfromtxt(os.path.join("results", "Abel", "arterial", "A" + str(Aindex) + ".txt"), delimiter=', ')
    data = np.genfromtxt(os.path.join("results", 'Erik', "arterial", "A" + str(Aindex) + ".txt"), delimiter=', ')
    
    dataT = data.T
    time = closest(list(dataT[0]),dataT[0][len(dataT[0])-1]-0.794)
    utolso_ciklus_index=list(dataT[0]).index(time)
    q = dataT[adatindex][utolso_ciklus_index:]
    t = dataT[0][utolso_ciklus_index:]
    #print(t)
    QQ = 0
    for Qindex in range(len(q)-1):
        QQ += (q[Qindex] + q[Qindex + 1]) * 0.5 * (t[Qindex+1] - t[Qindex])

    return (QQ/0.794*60*1e+06)

def calcCt(adatindex):

    #data = np.genfromtxt(os.path.join("results", "Abel", "arterial", "A" + str(Aindex) + ".txt"), delimiter=', ')
    data = np.genfromtxt(os.path.join("results", 'Bathsheba', "p10", "tissueO2.txt"), delimiter=', ')
    
    dataT = data.T
    time = closest(list(dataT[0]),dataT[0][len(dataT[0])-1]-0.794)
    utolso_ciklus_index=list(dataT[0]).index(time)
    q = dataT[adatindex][utolso_ciklus_index:]
    t = dataT[0][utolso_ciklus_index:]
    #print(t)
    QQ = 0
    for Qindex in range(len(q)-1):
        QQ += (q[Qindex] + q[Qindex + 1]) * 0.5 * (t[Qindex+1] - t[Qindex])

    return (QQ/0.794)

"""
AA=[1,8,12,55,79]
with open ('q_values.txt', 'w') as File_save:
    for index in range(len(AA)):
        #try:
        Q1 = calcQ(AA[index], 5)
        Q2 = calcQ(AA[index], 6)
        File_save.write('A' + str(AA[index]) + '  ' + str(Q1) + ' '+ str(Q2) + '\n')
        #except:
        print("")

"""

print(calcCt(1))