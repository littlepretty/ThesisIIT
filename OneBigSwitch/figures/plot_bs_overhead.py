import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', size=14)

data = np.loadtxt('bs_overhead.txt')

x = data[:, 2]
y = data[:, 3]
logx = np.log2(data[:, 2])
logy = np.log2(data[:, 3])

print(x)
print(y)

fig, ax = plt.subplots()

ax.loglog(x, y, linewidth=3.0, marker='>', markersize=16.0, color='b')
plt.grid(True)
plt.xticks(x, ['%d' % i for i in x])
plt.xlabel('#Rules Processed')
plt.ylabel('Running Time (Milliseconds)')
ax.set_xlim([220, 74000])
plt.title('Execution Time of OBS Abstraction Approach')
# ax.plot(logx, logy, 'b', linewidth=4.0, label='Overhead Trend')

# width = 0.4
# ax.bar(logx - width/2, logy, width, color='white', hatch='/')
# plt.xticks(logx, ['%.1f' % i for i in logx])
# plt.grid(True)
# plt.xlabel('$\log_2$(Number of Rules Processed)')
# plt.ylabel('$\log_2$(Running Time) (Milliseconds)')
# plt.legend(loc='upper left')

plt.tight_layout()
# plt.savefig('bs_overhead.eps', fmt='eps')
plt.savefig('bs_overhead.pdf', fmt='pdf')
plt.show()
