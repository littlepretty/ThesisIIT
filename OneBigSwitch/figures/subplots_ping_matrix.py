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

    fig, (ax1, ax2) = plt.subplots(2, sharey=True)

    cax1 = ax1.matshow(tree_matrix, cmap=plt.cm.gray)
    fig.colorbar(cax1)

    if (depth, fanout) == (4, 3):
        ax1.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
    else:
        ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))

    ax1.set_xticklabels(ticks)
    ax1.set_yticklabels(ticks)
    ax1.set_title('Ping Matrix of $net_1$', y=1.1)

    cax2 = ax2.matshow(bs_matrix, cmap=plt.cm.gray)

    if (depth, fanout) == (4, 3):
        ax2.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax2.yaxis.set_major_locator(ticker.MultipleLocator(10))
    else:
        ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax2.yaxis.set_major_locator(ticker.MultipleLocator(1))

    ax2.set_xticklabels(ticks)
    ax2.set_yticklabels(ticks)
    ax2.set_title('Ping Matrix of $net_2$', y=1.1)

    plt.xlabel('Destination Hosts')
    plt.ylabel('Source Hosts')
    plt.tight_layout()

    plt.savefig('comp_ping_mat_%d_%d.pdf' % (depth, fanout), format='pdf')
    plt.show()
