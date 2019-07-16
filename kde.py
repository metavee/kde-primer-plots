"""
Functions for manually constructing kernel density estimates.
"""


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def epa_kernel(x, x0):
    """
    Parabolic kernel function. Bandwidth is currently fixed.
    """

    y = 0.75 * (1 - (x - x0)**2)
    if type(y) == np.ndarray:
        y[y < 0] = 0

    return y


def kde(data, x_grid, kernel=epa_kernel):
    """
    Take some data and compute its kernel density estimate at each point on a specified grid.
    """

    results = np.zeros(x_grid.shape)
    for i, x0 in enumerate(x_grid):
        results[i] = sum(kernel(data, x0)) / len(data)

    return results


def plot_kde_varying_bw(data, bws):
    assert len(bws) == 6

    fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
    for ax, bw in zip(axes.flatten(), bws):
        plt.sca(ax)
        sns.kdeplot(data, bw=bw)
        sns.despine()

    # make big subplot with common axis
    # https://stackoverflow.com/a/36542971
    fig.add_subplot(111, frameon=False)
    plt.xticks(alpha=0)
    plt.yticks(alpha=0)
    plt.grid(False)

    plt.tight_layout()
