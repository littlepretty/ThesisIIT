#!/usr/bin/python3.7

from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
import glog as log

font = {'family': 'normal', 'size': 28}
matplotlib.rc('font', **font)
matplotlib.rcParams["figure.figsize"] = [14, 10]


def plotF1Improve(filepath: str):
    df = pd.read_csv(filepath, sep=',')
    print(df)
    x = range(0, df['Relative'].size)

    plt.plot(x, df['Relative'], 'r', ls=':', marker='+',
             linewidth=2, markersize=12.0, markeredgewidth=3,
             clip_on=False, label='Relative Improvement')
    plt.plot(x, df['Absolute'], 'b', ls='--', marker='x',
             linewidth=2, markersize=12.0, markeredgewidth=3,
             clip_on=False, label='Absolute Improvement')
    plt.xlim((0, len(x) - 1))
    plt.xticks(x, df['Family'], rotation=45)
    plt.ylim((-0.1, 0.7))
    plt.yticks([y / 10.0 for y in range(-1, 8, 1)])

    plt.ylabel('Improvement of F1 Scores')
    plt.grid(which='both', axis='both', ls='-.')
    plt.legend()
    plt.subplots_adjust(left=0.14, bottom=0.16, right=0.96, top=0.97)
    plt.savefig('YanAcfgF1Improve.eps', format='eps')
    log.info(f'Figure for YanAcfg saved to YanAcfgScores.eps')


if __name__ == '__main__':
    path = 'YANACFG_f1_cmp.csv'
    plotF1Improve(path)
