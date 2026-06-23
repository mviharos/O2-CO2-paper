import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


compartments = ['capillary']#no vein


concentrations = [
    r'$CO_{2,pla}$ $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{plasma})}\right]$',
    r'$CO_{2,rbc}$ $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{cytoplasm})}\right]$', 
    r'$HCO_{3,pla}$ $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{plasma})}\right]$', 
    r'$HCO_{3,rbc}$ $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{cytoplasm})}\right]$', 
    r'$HbCO_2$ $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{cytoplasm})}\right]$'
]


concentration_labels = ['CO2_pla',
                  'CO2_rbc', 
                  'HCO3_pla', 
                  'HCO3_rbc', 
                  'HbCO2']


def abrazol0D(i, cstart, cend, ax, con):
    data = pd.read_csv(os.path.join("results", "Bathsheba_CO2_pul", "p10", concentration_labels[con], 'capillary' + ".txt"), header=None)
    t = data[0]
    var_s = data[1]
    var_e = data[2]

    # Keep only last 5 seconds
    tmax = t.max()
    mask = t <= (tmax - 0.)
    #mask = t <= (10 + tmax*0)
    t = t[mask]

    t0 = t.iloc[0]
    t=t-t0
    var_s = var_s[mask]
    var_e = var_e[mask]


    ax.plot(t, var_s, color=cstart, linestyle='dashed', linewidth = 3)
    ax.plot(t, var_e, color=cend, linestyle='dashed', linewidth = 3)

def abrazol0D_exercise(i, cstart, cend, ax, con):
    data = pd.read_csv(os.path.join("results", "Bathsheba_exercise", "p10", concentration_labels[con], 'capillary' + ".txt"), header=None)
    t = data[0]
    var_s = data[1]
    var_e = data[2]

    # Keep only last 5 seconds
    tmax = t.max()
    mask = t >= (tmax - 5)
    t = t[mask]

    t0 = t.iloc[0]
    t=t-t0
    var_s = var_s[mask]
    var_e = var_e[mask]


    ax.plot(t, var_s, color=cstart, linestyle='dashed', linewidth = 3)
    ax.plot(t, var_e, color=cend, linestyle='dashed', linewidth = 3)



# Create figure with 5 rows and 5 columns
fig, ax = plt.subplots(1, 5, figsize=(25, 5))
fig.tight_layout(pad=2.0)

for col in range(5):  # loop over columns

    #if col == 0:
        #ax[col].set_ylabel('Arteries', fontsize = 18)
    ax[col].set_title(concentrations[col], fontsize = 18)
    ax[col].legend(['Aorta s.', 'Aorta e.',
                       'I. Carotid s.', 'I. Carotid e.',
                       'A. Tribial s.', 'A. Tribial e.',
                       'Radial s.', 'Radial e.'])

    # Row 3
    abrazol0D(1, 'darkorange', 'darkmagenta', ax[col],col)

    #abrazol0D_exercise(1, 'blue', 'black', ax[col],col)
    #if col == 0:
        #ax[col].set_ylabel('Capillary', fontsize = 18)
    ax[col].legend(['Capillary start', 'Capillary end'])
    ax[col].grid()



plt.tight_layout()
plt.savefig("PlasmaCO2.jpg", dpi=150)
