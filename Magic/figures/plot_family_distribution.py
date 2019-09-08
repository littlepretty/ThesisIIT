#!/usr/bin/python3.7
import time
import glog as log
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from typing import Dict, List


font = {'family': 'normal', 'size': 28}
matplotlib.rc('font', **font)
matplotlib.rcParams["figure.figsize"] = [14, 10]


def plotFamilyDist(data: str):
    dist = pd.read_csv('%s_train_label_distribution.csv' % data.upper())
    print(dist)
    indices = range(0, len(dist))
    print(indices)

    fig, ax = plt.subplots()
    barWidth = 0.65

    rects = ax.barh(indices, dist['Cnt'], barWidth,
                    color='white', hatch='/', edgecolor='black')
    ax.set_xlabel('#Instances in Dataset')
    ax.set_yticks(indices)
    ax.set_yticklabels(dist['Family'], rotation=0)
    if data.lower() == 'msacfg':
        ax.set_xlim((0, 3300))
    else:
        ax.set_xlim((0, 4400))

    cntMsAcfg = [1541, 2478, 2942, 475, 42, 751, 398, 1228, 1013]
    for (i, val) in enumerate(dist['Cnt']):
        if data.lower() == 'msacfg':
            ax.text(val, i + barWidth / 4, str(cntMsAcfg[i]))
        else:
            ax.text(val, i + barWidth / 3, str(val))

    ax.invert_yaxis()
    plt.subplots_adjust(left=0.15, bottom=0.10, right=0.96, top=0.99)
    plt.grid(ls='-.')
    plt.savefig('%sLabelDist.eps' % data, format='eps')
    log.info(f'Figure for {data} saved to {data}LabelDist.eps')
    # plt.show()


if __name__ == '__main__':
    log.setLevel("INFO")
    plotFamilyDist('MsAcfg')
    plotFamilyDist('YanAcfg')
