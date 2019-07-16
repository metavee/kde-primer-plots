import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


palette = sns.color_palette()


def plot_histogram(data, start=None, stop=None, n_bins=10, shift=0):
    if start is None:
        start = min(data)

    if stop is None:
        stop = max(data)

    bin_edges = np.linspace(start+shift, stop+shift, n_bins+1)
    plt.hist(data, bins=bin_edges)
    plt.xlim(start+shift, stop+shift)
    sns.despine()


def plot_hist_varying_nbins(data, bins, start=None, stop=None):
    assert len(bins) == 6

    fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
    for ax, n_bins in zip(axes.flatten(), bins):
        plt.sca(ax)
        plot_histogram(data, start, stop, n_bins=n_bins)

    # make big subplot with common axis
    # https://stackoverflow.com/a/36542971
    fig.add_subplot(111, frameon=False)
    plt.xticks(alpha=0)
    plt.yticks(alpha=0)
    plt.grid(False)

    plt.tight_layout()


def plot_hist_varying_shift(data, shifts, start=None, stop=None, n_bins=20):
    assert len(shifts) == 6

    fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)
    for ax, shift in zip(axes.flatten(), shifts):
        plt.sca(ax)
        plot_histogram(data, start, stop, n_bins=n_bins, shift=shift)

    # make big subplot with common axis
    # https://stackoverflow.com/a/36542971
    fig.add_subplot(111, frameon=False)
    plt.xticks(alpha=0)
    plt.yticks(alpha=0)
    plt.grid(False)

    plt.tight_layout()
