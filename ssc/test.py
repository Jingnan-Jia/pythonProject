import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("score_labels_5_mul_by_237_distribution.csv")

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
bins = np.arange(0, 105, 5)
fig = plt.figure(figsize=(15, 2))
plt.subplots_adjust(left=0, bottom=None, right=1, top=None, wspace=0, hspace=0)

for plot_id, column in enumerate(data.columns[1:]):
    ax = fig.add_subplot(1, 3, plot_id + 1)
    x_ = data['Label'].to_numpy().reshape(-1, )
    label = data[column].to_numpy().reshape(-1, )
    scatter_kwds = {'facecolor': colors[plot_id], 'width':4}
    ax.bar(x_, label, **scatter_kwds)
    for i, v in zip(x_, label):
        ax.text(i, v+20, str(v), ha='center', color='black')

    ax.set_xlabel("Score", fontsize=15)
    ax.set_xticks([i * 5 for i in range(21)])

    ax.set_xticklabels([i * 5 for i in range(21)])
    ax.set_ylim(0, 800)
    ax.set_xlim(-4, 104)

    ax.text(50, 600, column, ha='center', fontsize=15,color='black')
    # ax.set_title(column, fontsize=15, pad=100)
    if plot_id == 0:
        ax.set_ylabel("Count", fontsize=15)
    #     for i in range(21):
    #         plt.text(arr[1][i],arr[0][i],str(arr[0][i]))
    else:
        ax.axes.yaxis.set_visible(False)
fig.tight_layout()
#         ax.set_axis_off()

plt.savefig('test.jpg')