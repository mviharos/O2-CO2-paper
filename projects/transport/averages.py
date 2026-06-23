import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

stuff = ["CO2_pla", "CO2_rbc", "HCO3_pla", "HCO3_rbc", "HbCO2"]
weights = [0.56, 0.44, 0.56, 0.44, 0.44]

def calculate_time_weighted_average( variable, t0):
    data = np.loadtxt(os.path.join("results",'Bathsheba_CO2_pul', "p10", variable , "capillary.txt"), delimiter=",")
    
    # Csak azok az adatok, amelyek t0 után vannak
    filtered_data = data[data[:, 0] > t0]

    if len(filtered_data) < 2:
        raise ValueError("Nincs elég adat t0 után az időátlag számításához.")

    times = filtered_data[:, 0]
    values = filtered_data[:, 2]

    # Időkülönbségek a trapezoid szabályhoz
    dt = np.diff(times)
    avg_values = (values[:-1] + values[1:]) / 2

    # Időátlag kiszámítása
    weighted_integral = np.sum(avg_values * dt)
    total_time = times[-1] - times[0]
    time_avg = weighted_integral / total_time

    return time_avg

# Használat példa:
t0 = 35.0-0.9242  

sum  = 0.0

values = []

for i in range(len(stuff)):
    avg = calculate_time_weighted_average( stuff[i], t0)
    sum = sum +avg*weights[i]
    print(stuff[i] + f" : {avg:.8f}")
    values.append(avg*weights[i])

print(sum)


print()
print()

for i in range(len(stuff)):
    print(stuff[i] + "  " +str(values[i]/sum))
