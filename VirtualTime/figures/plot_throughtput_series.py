import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


mpl.rc('font', size=28)
data = np.loadtxt('ThroughputHistory10G.txt',
                  skiprows=1)
tdf1 = data[:, 0]
tdf4 = data[:, 1]
testbed = data[:, 2]

index = np.arange(0, len(tdf1))
fig, ax = plt.subplots()
ax.plot(tdf1, color='b', marker='s', label='TDF = 1')
ax.plot(tdf4, color='r', marker='D', label='TDF = 4')
ax.plot(testbed, color='g', marker='v', label='Physical Testbed')

ax.set_ylabel('Throughput (Gpbs)')
ax.set_xlabel('Execution Time (s)')
ax.set_xlim([0, 50])
ax.set_ylim([0, 10])
plt.grid(color='k', linestyle=':', linewidth=1)
plt.legend(loc='lower right')
plt.show()
