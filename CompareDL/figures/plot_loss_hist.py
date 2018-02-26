import pickle
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', size=28)
filename = open('5Fold160.pkl', 'rb')
hist = pickle.load(filename)

fig, ax1 = plt.subplots()
print(hist.keys())
ax1.plot(hist['train_loss'] / 4.0, 'r--', label='Trainset', linewidth=4)
ax1.plot(hist['valid_loss'], 'b:', label='Validset', linewidth=4)
ax1.set_ylabel('Average Loss')
ax1.set_xlim([-5, 165])
ax1.set_xlabel('Training Time(Epochs)')
ax1.legend(loc='upper right')
ax1.grid(color='k', linestyle=':', linewidth=1)
# fig.tight_layout()
plt.savefig('history.pdf', format='pdf')
plt.show()
