import os

import numpy as np

output_dir = 'plots'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# switch CWD to output dir for convenience
curdir = os.path.abspath(os.getcwd())
os.chdir(output_dir)

import matplotlib.pyplot as plt
import seaborn as sns

import bootstrap
import kde
import kde_construction
import histogram
import marks
from quantile import plot_quantile
import trimodal_dist

sns.set_style('white')

def make_marks_figures():
    marks_percent = marks.gen_marks(12345)

    plt.figure()
    histogram.plot_histogram(marks_percent, 0, 100, n_bins=20)
    plt.xlabel('Marks (%)')
    plt.ylabel('Count')
    plt.savefig('marks_hist.svg')
    plt.clf()

    plot_quantile(marks_percent)
    plt.xlabel('Percentile')
    plt.ylabel('Marks (%)')
    plt.savefig('marks_quantile.svg')
    plt.clf()

    sns.kdeplot(marks_percent, kernel='gau', bw=0.15, gridsize=1000)
    sns.despine()
    plt.xlabel('Marks (%)')
    plt.ylabel(r'$\rho(\operatorname{Marks})$')
    plt.savefig('marks_kde.svg')
    plt.clf()

    sns.distplot(marks_percent, bins=20, kde_kws={'bw': 0.15, 'gridsize': 1000})
    sns.despine()
    plt.xlabel('Marks (%)')
    plt.ylabel(r'$\rho(\operatorname{Marks})$')
    plt.savefig('marks_kde_bndry.svg')

    bws = np.linspace(0.05, 0.3, 6)
    kde.plot_kde_varying_bw(marks_percent, bws)
    plt.xlabel('Marks (%)')
    plt.ylabel(r'$\rho(\operatorname{Marks})$')
    plt.savefig('marks_kde_bws.svg')
    plt.close()


def make_trimodal_figures():
    xs = trimodal_dist.make_dataset(100, seed=2468)

    plt.figure()

    # KDE
    sns.kdeplot(xs, bw=0.25)
    sns.despine()
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\rho(x)$')
    plt.savefig('trimodal_kde.svg')
    plt.clf()

    # histograms with varying bin shift and bin width
    bin_start = min(xs)
    bin_stop = max(xs)
    n_bins = 20
    bin_width = (bin_stop - bin_start) / float(n_bins)
    shifts = np.arange(6) * bin_width / 4

    histogram.plot_hist_varying_shift(xs, shifts, bin_start, bin_stop, n_bins)
    plt.xlabel('$x$')
    plt.ylabel('Count')
    plt.savefig('trimodal_hist_shift.svg')
    plt.clf()

    bins = np.linspace(10, 40, 6).astype('int')
    histogram.plot_hist_varying_nbins(xs, bins, bin_start, bin_stop)
    plt.xlabel('$x$')
    plt.ylabel('Count')
    plt.savefig('trimodal_hist_nbins.svg')
    plt.clf()

    # plot of the underlying probability distribution with KDE
    x_num, y_num = trimodal_dist.trimodal_pdf(1000)

    # true dist with ticks
    plt.plot(x_num, y_num)
    sns.rugplot(xs)
    sns.despine()
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\rho(x)$')
    plt.savefig('trimodal_dist_ticks.svg')
    plt.clf()

    plt.plot(x_num, y_num, label='True distribution')
    sns.kdeplot(xs, bw=0.25, label='KDE')
    sns.despine()
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\rho(x)$')
    plt.legend()
    plt.savefig('trimodal_prob_dist_kde.svg')
    plt.clf()

    # quantile plot
    plot_quantile(xs)
    plt.xlabel('Percentile')
    plt.ylabel('$x$')
    plt.savefig('trimodal_quantile.svg')
    plt.clf()

    # confidence interval
    bootstrap.plot_kde_uncertainty(xs)
    plt.xlabel('$x$')
    plt.ylabel(r'$\rho(x)$')
    plt.savefig('trimodal_kde_uncertainty.svg')

    plt.close()


def make_kde_construction_figures():
    x_grid = np.linspace(-3, 3, 200)

    plt.figure()

    plt.plot(x_grid, kde.epa_kernel(x_grid, 0))
    plt.xlabel('$x$')
    plt.ylabel('$K_0(x)$')
    sns.despine()
    plt.savefig('kernel.svg')
    plt.clf()

    tiny_data = np.array([-0.95, 0.75, 1.00])

    kde_construction.animate_kde_construction(tiny_data, x_grid)
    kde_construction.inverted_plot_contribution(tiny_data, x_grid)    

    plt.close()

make_marks_figures()
make_trimodal_figures()
make_kde_construction_figures()

# go back to original CWD
os.chdir(curdir)