"""
Functions for plotting a bootstrapped confidence interval of a KDE.
"""


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from kde import kde


def sample_with_replacement(data):
    """
    Sample the provided data (with replacement) and return a new dataset of the same size.
    """

    return data[np.random.randint(0, len(data), len(data))].copy()


def plot_kde_uncertainty(data, n_resamples=1000, x_resolution=1000, significance=0.05, palette=sns.color_palette()):
    """
    Bootstrap a confidence interval for the KDE of the provided dataset, and plot along with the KDE.
    """

    assert n_resamples >= 100

    x_grid = np.linspace(min(data), max(data), x_resolution)
    orig_kde = kde(data, x_grid)

    resampled_kdes = np.zeros((n_resamples, x_resolution))

    for i in range(n_resamples):
        resample = sample_with_replacement(data)
        resampled_kdes[i] = kde(resample, x_grid)

    # sort to get percentiles
    resampled_kdes.sort(axis=0)

    def percentile_index(percentile, N):
        """
        Find the index of the x'th percentile in a sorted collection of size N.
        """

        assert 0 <= percentile <= 1

        return int(np.round(percentile * N))

    def ci_index(alpha, N):
        """
        Find the indices in a sorted collection of size N of the two bounds of a confidence interval of significance level alpha.
        """

        return percentile_index(alpha/2., N), percentile_index((1. - alpha/2.), N)

    i_lower, i_higher = ci_index(significance, n_resamples)
    plt.plot(x_grid, resampled_kdes[i_lower], '--', color=palette[0])
    plt.plot(x_grid, resampled_kdes[i_higher], '--', color=palette[0])

    plt.plot(x_grid, orig_kde, '-', color=palette[0])
    sns.despine()
