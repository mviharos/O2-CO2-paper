from scipy.optimize import minimize
from scipy.optimize import differential_evolution
import pandas as pd
import numpy as np
import os
from scipy.signal import argrelextrema


def ff(x):

	f = str(x)

	os.system('./transport.out ' + f)


# base model parameters
x0 = [1., 1.05, 1.1, 1.15, 1.2, 1.25, 0.95, 0.9, 0.85, 0.8, 0.75]

names = ['N1','N1_05','N1_1','N1_15','N1_2','N1_25','N0_95','N0_9','N0_85','N0_8','N0_75']



for index in range(len(x0)):

	#print(" [*] running case" + str(index))
	ff(x0[index])
	#print(" [*] running case: OK" + str(index))
	os.rename("./results//Bathsheba", "results//" + names[index])


