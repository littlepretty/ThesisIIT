import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker

matplotlib.rc('font', size=18)

for depth in (2, 4):
    fanout = 3
    tree_matrix = np.loadtxt('ping_matrix_%d_%d.txt' % (depth, fanout))
    bs_matrix = np.loadtxt('bs_ping_matrix_%d_%d.txt' % (depth, fanout))

    if (depth, fanout) == (4, 3):
        ticks = [str(x) for x in range(-10, len(tree_matrix) + 1, 10)]
    else:
        ticks = [str(x) for x in range(0, len(tree_matrix) + 1, 1)]

    fig, ax = plt.subplots()
    cax = ax.matshow(tree_matrix, cmap=plt.cm.gray)
    fig.colorbar(cax)

    if (depth, fanout) == (4, 3):
        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    else:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    ax.set_xticklabels(ticks)
    ax.set_yticklabels(ticks)

    plt.xlabel('Destination Hosts')
    plt.ylabel('Source Hosts')
    plt.title('Ping Matrix of $net_1$', y=1.1)
    plt.tight_layout()

    plt.savefig('ping_mat_%d_%d.pdf' % (depth, fanout), format='pdf')
    plt.show()

    fig, ax = plt.subplots()
    cax = ax.matshow(bs_matrix, cmap=plt.cm.gray)
    fig.colorbar(cax)

    if (depth, fanout) == (4, 3):
        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    else:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    ax.set_xticklabels(ticks)
    ax.set_yticklabels(ticks)

    plt.xlabel('Destination Hosts')
    plt.ylabel('Source Hosts')
    plt.title('Ping Matrix of $net_2$', y=1.1)
    plt.tight_layout()

    plt.savefig('bs_ping_mat_%d_%d.pdf' % (depth, fanout), format='pdf')
    plt.show()
