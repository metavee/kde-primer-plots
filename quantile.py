import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_quantile(data):
    plt.figure()
    order_stat = 100 * (np.arange(1, data.size+1) - 0.5) / data.size # = (k - 0.5) / n
    plt.plot(order_stat, sorted(data), 'o')
    sns.despine()
