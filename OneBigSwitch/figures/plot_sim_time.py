import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rc('font', size=14)
data = np.loadtxt('s3f_sim_time.txt', comments='#')

bs_mean = np.zeros(5, dtype=float)
bs_std = np.zeros(5, dtype=float)
tree_mean = np.zeros(5, dtype=float)
tree_std = np.zeros(5, dtype=float)

for i in range(0, len(data), 5):
    tree_mean[i/5] = np.mean(data[i:i+5, 2]) * 1000
    tree_std[i/5] = np.std(data[i:i+5, 2]) * 1000
    bs_mean[i/5] = np.mean(data[i:i+5, 3]) * 1000
    bs_std[i/5] = np.std(data[i:i+5, 3]) * 1000.0

print(tree_mean)
print(bs_mean)
speedup = np.divide(tree_mean, bs_mean)
reduction = np.divide(tree_mean - bs_mean, tree_mean)
print(reduction)
print(speedup)
print('Avg Speedup = %.4f' % np.mean(speedup))

width = 4
ticks = range(10, 60, 10)
scale_tree = [x - width for x in ticks]
scale_bs = [x for x in ticks]

fig, ax = plt.subplots()
ax.bar(scale_tree, tree_mean, width, color='b', hatch='/',
       error_kw=dict(ecolor='red', lw=4, capsize=5, capthick=2),
       yerr=tree_std, label='Tree Network')
ax.bar(scale_bs, bs_mean, width, color='r', hatch='\\', yerr=bs_std,
       error_kw=dict(ecolor='blue', lw=4, capsize=5, capthick=2),
       label='Big-Switch Network')

plt.xticks(ticks, ['(2,3)', '(2,4)', '(3,3)', '(3,4)', '(4,3)'])
plt.grid(True)
plt.legend(loc='upper left')
plt.xlabel('Tree-Topology Network Settings')
plt.ylabel('Simulation Execution Time (Milliseconds)')
plt.title('Simulation Time Reduced by OBS Model')
plt.tight_layout()
# eps format doesn't support transparency
plt.savefig('comp_sim_time.pdf', fmt='pdf')
plt.show()
