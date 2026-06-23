import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# -------------------------
# Configuration
# -------------------------

# CO2 variables and weights
co2_variables = ["CO2_pla", "CO2_rbc", "HCO3_pla", "HCO3_rbc", "HbCO2"]
co2_weights   = [0.56,      0.44,      0.56,       0.44,       0.44]

# O2 variables and weights
o2_variables = ["HB_O2", "C_Plasma_O2"]
o2_weights   = [0.44,    0.56]

n_points = [136, 190, 266, 372, 522]

models = [
    "Bathsheba_CO2_pul_n1",
    "Bathsheba_CO2_pul",
    "Bathsheba_CO2_pul_1",
    "Bathsheba_CO2_pul_2",
    "Bathsheba_CO2_pul_3"
]

finest_model = "Bathsheba_CO2_pul_3"
base_path    = "results"
t0           = 80.0 - 0.9242


# -------------------------
# Helper functions
# -------------------------

def calculate_time_weighted_average(file_path, t0):
    data     = np.loadtxt(file_path, delimiter=",")
    filtered = data[data[:, 0] > t0]

    if len(filtered) < 2:
        raise ValueError(f"Not enough data after t0 in {file_path}")

    times  = filtered[:, 0]
    values = filtered[:, 2]

    dt         = np.diff(times)
    avg_values = (values[:-1] + values[1:]) / 2

    weighted_integral = np.sum(avg_values * dt)
    total_time        = times[-1] - times[0]

    return weighted_integral / total_time


def compute_results(models, variables, weights, subfolder, filename):
    """Load data, compute time-weighted averages and weighted sum for a set of variables."""
    results = pd.DataFrame(index=models, columns=variables)

    for model in models:
        for var in variables:
            file_path = os.path.join(base_path, model, subfolder, var, filename)
            avg = calculate_time_weighted_average(file_path, t0)
            results.loc[model, var] = avg

    results = results.astype(float)

    results["Weighted_sum"] = sum(
        results[var] * w for var, w in zip(variables, weights)
    )

    return results


def normalize(results, finest_model):
    return results / results.loc[finest_model]


def plot_panel(ax, n_points, normalized, variables, title):
    """Plot normalized convergence curves on a given Axes."""
    for var in variables:
        ax.plot(n_points, normalized[var], marker='o', label=var)

    ax.plot(
        n_points,
        normalized["Weighted_sum"],
        marker='o',
        linewidth=3,
        label="Weighted sum"
    )

    ax.axhline(1.0, linestyle="--", color="black", linewidth=0.8)
    ax.set_xlabel("Number of mesh points")
    ax.set_ylabel("Normalized value")
    ax.set_title(title)
    ax.legend(fontsize=8)
    ax.grid(True)


# -------------------------
# Compute all four datasets
# -------------------------

print("Computing CO2 – Systemic (venous)...")
co2_sys  = compute_results(models, co2_variables, co2_weights, subfolder="p10",           filename="capillary.txt")
print("Computing CO2 – Pulmonary (arterial)...")
co2_pul  = compute_results(models, co2_variables, co2_weights, subfolder="heart_kim_lit", filename="pul_cap.txt")

print("Computing O2 – Systemic...")
o2_sys   = compute_results(models, o2_variables,  o2_weights,  subfolder="p10",           filename="capillary.txt")
print("Computing O2 – Pulmonary...")
o2_pul   = compute_results(models, o2_variables,  o2_weights,  subfolder="heart_kim_lit", filename="pul_cap.txt")

# Normalize
co2_sys_norm = normalize(co2_sys,  finest_model)
co2_pul_norm = normalize(co2_pul,  finest_model)
o2_sys_norm  = normalize(o2_sys,   finest_model)
o2_pul_norm  = normalize(o2_pul,   finest_model)

# Print summaries
for label, df in [
    ("CO2 Systemic (raw)",   co2_sys),
    ("CO2 Pulmonary (raw)",  co2_pul),
    ("O2 Systemic (raw)",    o2_sys),
    ("O2 Pulmonary (raw)",   o2_pul),
]:
    print(f"\n{label}\n")
    print(df)

for label, df in [
    ("CO2 Systemic (normalized)",   co2_sys_norm),
    ("CO2 Pulmonary (normalized)",  co2_pul_norm),
    ("O2 Systemic (normalized)",    o2_sys_norm),
    ("O2 Pulmonary (normalized)",   o2_pul_norm),
]:
    print(f"\n{label}\n")
    print(df)

# -------------------------
# 2x2 plot
# -------------------------

fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Mesh Independence Analysis (Normalized)", fontsize=14, fontweight="bold")

plot_panel(axes[0, 0], n_points, co2_sys_norm, co2_variables, "CO2 – Systemic (Venous)")
plot_panel(axes[0, 1], n_points, co2_pul_norm, co2_variables, "CO2 – Pulmonary (Arterial)")
plot_panel(axes[1, 0], n_points, o2_sys_norm,  o2_variables,  "O2 – Systemic (Venous)")
plot_panel(axes[1, 1], n_points, o2_pul_norm,  o2_variables,  "O2 – Pulmonary (Arterial)")

plt.tight_layout()
plt.savefig("mesh_combined.jpg", dpi=150)
print("\nSaved mesh_combined.jpg")
