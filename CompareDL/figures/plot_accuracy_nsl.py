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
machines = ['SVM', 'MLP', 'RBM', 'SAE', 'WnD']
accuracy = [78.5353, 78.6639, 78.8058, 79.3426, 78.9567]
precision = [81.5500, 82.0900, 82.0100, 82.1300, 82.1100]
recall = [78.5400, 78.6600, 78.8100, 79.3400, 78.9400]
# train_accuracy = [99.2077, 99.3966, 99.4912, 99.3449, 99.7261]
# train_std =      [0.00000, 0.0246,  0.0231,  0.0216,  0.0121]
# test_std =       [0.00000, 0.5162,  0.3499,  0.4215,  0.0813]

width = 0.93
ind = np.arange(0, len(machines) * 3, 3)
fig, ax = plt.subplots()

rects1 = ax.bar(
    ind,
    accuracy,
    width,
    color='w',
    edgecolor='r',
    hatch='/',
    label='Accuracy')
rects2 = ax.bar(
    ind + width,
    precision,
    width,
    color='w',
    edgecolor='b',
    hatch='\\',
    label='Precision')
rects3 = ax.bar(
    ind + 2 * width,
    recall,
    width,
    color='w',
    edgecolor='g',
    hatch='//',
    label='Recall')

ax.set_ylabel('Testset Performance(%)')
ax.set_xlabel('Classifiers')
ax.set_xticks(ind + width)
ax.set_xticklabels(machines)
ax.set_xlim([-.8, len(machines) * 3])
ax.set_ylim([60, 85])
plt.grid(color='k', linestyle=':', linewidth=1)
plt.legend(loc='lower right')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()
