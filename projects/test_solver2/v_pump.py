import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

cases = ['Abel_0d_pre', 'Abel_0d_pre']
models = 'p10'
elements = ['P3','g']

mmHg_to_Pa = 133.3616

# beolvasás
data = pd.read_csv(os.path.join("results",cases[0], models, elements[0] + ".txt"), header=None)
p1 = data[1]

data = pd.read_csv(os.path.join("results",cases[0], models, elements[1] + ".txt"), header=None)
p2 = data[1]

data = pd.read_csv(os.path.join("results",cases[0], models, "C3" + ".txt"), header=None)
q = data[1]

# utolsó 1000 elem kiválasztása
#p1 = p1[-1000:]
#p2 = p2[-1000:]
#q = q[-1000:]

# ábra
plt.figure(figsize=(12,6))
plt.plot(q, p1 - p2)

plt.grid()
plt.xlabel("q")
plt.ylabel("dp")

plt.savefig("csirke.png")

