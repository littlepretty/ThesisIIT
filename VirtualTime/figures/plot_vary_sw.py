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
sw = ('20', '40', '60', '80', '100')
data = np.loadtxt('vary_sw_scale.txt', skiprows=1)
data = data / 1000.0
avgs_tdf1 = data[:, 0]
avgs_tdf4 = data[:, 1]
stds_tdf1 = data[:, 2]
stds_tdf4 = data[:, 3]

width = 0.3
ind = np.arange(0, len(sw))
fig, ax = plt.subplots()
rects1 = ax.bar(ind, avgs_tdf1, width, color='b', yerr=stds_tdf1,
                edgecolor='k', hatch='/', label='TDF = 1')
rects2 = ax.bar(ind + width, avgs_tdf4, width, color='r', yerr=stds_tdf4,
                edgecolor='k', hatch='\\', label='TDF = 4')
ax.set_ylabel('Throughput (Gbps)')
ax.set_xlabel('#Switches')
ax.set_xticks(ind + width)
ax.set_xticklabels(sw)
ax.set_ylim([0, 6])

plt.grid(color='k', linestyle=':', linewidth=1)
plt.legend(loc='upper left')
plt.show()
