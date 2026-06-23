from scipy.optimize import minimize
import pandas as pd
import numpy as np
import os
from scipy.signal import argrelextrema

def ff_test(x):
	return x[0]**2+x[1]**2

def ff(x):
	# string for os.system
	s = './vpd_ref.out'
	for i in x:
		s = s + ' ' + str(i)

	# running the actual simulation
	os.system(s);

	# for output
	simulation = np.empty((1,len(literature)))

	# loading stuff for ff
	data = pd.read_csv("output.csv",header=None)
	simulation = data[0]

	df = (literature - simulation)/literature
	df = w*df
	ff = np.sqrt(np.sum(np.square(df), axis=0)/np.sum(w))

	with open(out_file_name, "a") as out_file:
		out_file.write("\n%-8.5f" % (ff))
		for sim in simulation:
			out_file.write(", %-8.5f" % (sim))
		for xx in x:
			out_file.write(", %-8.5f" % (xx))

	return ff

out_file_name = "log_nm_10.txt"
case_name = "Reymond_99_heart"
element_name = "arterial"

# rad_dia, rad_sys, aor_dia, aor_sys, car_dia, car_sys [mmHg]
# fem_q, cardiac_output, ica_q, ica_q_max, vertebralis_q, vertebralis_q_max [ml/min]
# PWV: aortic, car-fem, bra-rad, fem-ank [m/s]
literature = np.array([65.,123.,65.,103.,75.58,122.78,350.4,4570.,235.,385.,75.,142.8,7.63,8.1,10.43,9.79])

w = np.array([1.0,1.0,1.0,1.0,1.0,1.0,0.1,2.0,0.5,0.1,0.5,0.1,1.0,1.0,1.0,1.0])

x0 = [0.93,1.15,0.88,3.87,31.81,32.14,11.74,35.04,21.92,2.14,19.41,4.02,27.31,1.71,33.06,3.03,35.28,3.09,38.55,1.07,0.99,1.14,1.09,0.88,1.02,1.10,0.80,1.08,0.99,0.99,1.23,1.40,1.06,0.77,0.58,1.41,1.56,0.56,1.09]
#result = ff(x0)
#print("results: " + str(result))

print("[*] Start minizing...")
res = minimize(ff, x0, method='BFGS')
print("[*] Optimization ended")
print("  Solution: " + str(res.x))
print("	Final ff: " + str(res.fun))
print("	FF calls: " + str(res.nfev))


#locmin1 = argrelextrema(np.array (p),np.less, order=100)
#locminArray = np.asarray(locmin1)
#locminArraySize = locminArray.size
#locminArrayCutIndex = locminArray[0][locminArraySize-1]
#t1p = t1[locminArrayCutIndex]

