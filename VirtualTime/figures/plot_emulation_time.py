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
data = np.loadtxt('runtime.txt', skiprows=1)
avgs_tdf1 = data[:, 0]
avgs_tdf4 = data[:, 1]

width = 0.3
ind = np.arange(0, len(sw))
fig, ax = plt.subplots()
rects1 = ax.bar(ind, avgs_tdf1, width, color='b',
                hatch='/', edgecolor='k', label='Mininet-Hifi')
rects2 = ax.bar(ind + width, avgs_tdf4, width, color='r',
                hatch='\\', edgecolor='k', label='TDF = 4')
ax.set_ylabel('Running Time (Second)')
ax.set_xlabel('#Switches')
ax.set_xticks(ind + width)
ax.set_xticklabels(sw)
ax.set_ylim([200, 1200])
plt.grid(color='k', linestyle=':', linewidth=1)
plt.legend(loc='upper right')
plt.show()
