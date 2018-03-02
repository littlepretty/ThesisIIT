from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.,
            1.005 * height,
            '%.1f' % height,
            ha='center',
            va='bottom')


matplotlib.rc('font', size=28)
data = np.loadtxt('vary_bw.txt', skiprows=1)
avgs = np.mean(data, axis=0, keepdims=False) / 1000.0
stds = np.std(data, axis=0, keepdims=False) / 1000.0
print(avgs, stds)
avgs_tdf1 = [avgs[0], avgs[2], avgs[4]]
avgs_tdf4 = [avgs[1], avgs[3], avgs[5]]
testbed = [3.8, 7.6, avgs[6]]

stds_tdf1 = [stds[0], stds[2], stds[4]]
stds_tdf4 = [stds[1], stds[3], stds[5]]
stds_testbed = [0.001, 0.001, 0.001]
links = ('4', '8', '10')

width = 0.73
ind = np.arange(0, 3 * 3, 3)
fig, ax = plt.subplots()
rects1 = ax.bar(ind, avgs_tdf1, width, color='b', yerr=stds_tdf1,
                hatch='/', label='TDF = 1')
rects2 = ax.bar(ind + width, avgs_tdf4, width, color='r', yerr=stds_tdf4,
                hatch='\\', label='TDF = 2')
rects3 = ax.bar(ind + 2 * width, testbed, width, color='g', yerr=stds_testbed,
                hatch='//', label='Physical Testbed')
ax.set_ylabel('Throughput (Gbps)')
ax.set_xlabel('Link Bandwidth (Gbps)')
ax.set_xticks(ind + width)
ax.set_xticklabels(links)
ax.set_ylim([2, 10])

plt.grid(color='k', linestyle=':', linewidth=1)
plt.legend(loc='upper left')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()
