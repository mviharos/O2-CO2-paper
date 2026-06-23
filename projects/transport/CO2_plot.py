import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

elements = ['A1', 'A12', 'A55', 'A8']
compartments = ['arteriole', 'capillary', 'venulare']#no vein


concentrations = [
    r'CO2_pla $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{plasma})}\right]$',
    r'CO2_rbc $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{cytoplasm})}\right]$', 
    r'HCO3_pla $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{plasma})}\right]$', 
    r'HCO3_rbc $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{cytoplasm})}\right]$', 
    r'HbCO2 $\left[\frac{m^3 (CO_2)}{m^3 (\mathrm{cytoplasm})}\right]$'
]


concentration_labels = ['CO2_pla',
                  'CO2_rbc', 
                  'HCO3_pla', 
                  'HCO3_rbc', 
                  'HbCO2']

def abrazol(i, cstart, cend, ax, var_num):
    print(var_num)
    data = pd.read_csv(os.path.join("results", "Bathsheba", "arterial", elements[i] + ".txt"), header=None)
    t = data[0]
    var_s = data[var_num]#17
    var_e = data[var_num+1]#18

    # Keep only last 5 seconds
    tmax = t.max()
    mask = t >= (tmax - 5)
    t = t[mask]

    t0 = t.iloc[0]
    t=t-t0
    var_s = var_s[mask]
    var_e = var_e[mask]


    ax.plot(t, var_s, color=cstart, linewidth = 3)
    ax.plot(t, var_e, color=cend, linewidth = 3)

def abrazol0D(i, cstart, cend, ax, con):
    data = pd.read_csv(os.path.join("results", "Bathsheba", "p10", concentration_labels[con], compartments[i] + ".txt"), header=None)
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
fig, ax = plt.subplots(4, 5, figsize=(25, 20))
fig.tight_layout(pad=2.0)

for col in range(5):  # loop over columns
    # Row 1
    abrazol(0, 'pink', 'deeppink', ax[0, col], col*2 + 19)
    abrazol(1, 'yellow', 'goldenrod', ax[0, col], col*2 + 19)
    abrazol(2, 'lightblue', 'blue', ax[0, col], col*2 + 19)
    abrazol(3, 'olivedrab', 'darkgreen', ax[0, col], col*2 + 19)
    if col == 0:
        ax[0, col].set_ylabel('Arteries', fontsize = 18)
    ax[0, col].set_title(concentrations[col], fontsize = 18)
    ax[0, col].legend(['Aorta s.', 'Aorta e.',
                       'I. Carotid s.', 'I. Carotid e.',
                       'A. Tribial s.', 'A. Tribial e.',
                       'Radial s.', 'Radial e.'])
    ax[0, col].grid()

    # Row 2
    abrazol0D(0, 'darkorange', 'darkmagenta', ax[1, col],col)
    if col == 0:
        ax[1, col].set_ylabel('Arteriole', fontsize = 18)
    ax[1, col].legend(['Arteriole s.', 'Arteriole e.'])
    ax[1, col].grid()

    # Row 3
    abrazol0D(1, 'darkorange', 'darkmagenta', ax[2, col],col)
    if col == 0:
        ax[2, col].set_ylabel('Capillary', fontsize = 18)
    ax[2, col].legend(['Capillary s.', 'Capillary e.'])
    ax[2, col].grid()

    # Row 4
    abrazol0D(2, 'darkorange', 'darkmagenta', ax[3, col],col)
    if col == 0:
        ax[3, col].set_ylabel('Venulare', fontsize = 18)
    ax[3, col].legend(['Venulare s.', 'Venulare e.'])
    ax[3, col].grid()
    ax[3, col].set_xlabel('Time [s]', fontsize = 18)


plt.tight_layout()
plt.savefig("PlasmaCO2.jpg", dpi=150)
