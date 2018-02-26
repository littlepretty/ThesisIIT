import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


matplotlib.rc('font', size=14)

bs_data = np.loadtxt('bs_emu_resource.txt')
tree_data = np.loadtxt('tree_emu_resource.txt')
bs_rules = bs_data[:, 2]
tree_rules = tree_data[:, 2]

width = 4
ticks = [10, 20, 30, 40, 50]
scale_tree = [x - width for x in ticks]
scale_bs = [x for x in ticks]

fig, ax = plt.subplots()
rects1 = ax.bar(scale_tree, tree_rules, width, color='b', hatch='/',
                label='Tree Topology')
rects2 = ax.bar(scale_bs, bs_rules, width, color='r', hatch='\\',
                label='Big Switch')
print(tree_rules)
print(bs_rules)
reduction = np.divide(tree_rules - bs_rules, tree_rules)
print(reduction)

autolabel(rects1)
autolabel(rects2)

plt.yscale('log')
plt.xticks(ticks, ['(2,3)', '(2,4)', '(3,3)', '(3,4)', '(4,3)'])
plt.grid(True)
plt.legend(loc='upper left')
plt.xlabel('Tree-Topology Network Settings')
plt.ylabel('Total Number of Rules')
plt.title('Number of Rules Reduced by OBS Model')
plt.tight_layout()

# eps format doesn't support transparency
plt.savefig('comp_num_rules.pdf', fmt='pdf')
plt.show()
