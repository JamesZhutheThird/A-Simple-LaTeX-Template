import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-np.pi, 5 * np.pi, 200, endpoint=True)
it = [np.sin(t_) if t_ > 0 else 0 for t_ in t]
vt = [np.sin(t_) * (1 - np.cos(t_)) if t_ > 0 else 0 for t_ in t]

# v-i graph
plt.figure(figsize=(4, 4))
plt.plot(it, vt)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel('i')
plt.ylabel('v')
plt.xticks(np.linspace(-1.5, 1.5, 7))
plt.yticks(np.linspace(-1.5, 1.5, 7))
plt.savefig('problem1.pdf')
plt.show()