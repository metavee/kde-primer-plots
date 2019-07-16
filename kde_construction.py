from kde import *

import os

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


palette = sns.color_palette()

output_frames_dir = 'kde_construction_convolution'
if not os.path.exists(output_frames_dir):
    os.makedirs(output_frames_dir)


def animate_kde_construction(data, x_grid):
    y_grid = kde(data, x_grid, epa_kernel)

    num_zeros = int(np.ceil(np.log10(len(x_grid))))
    fn_format = os.path.join(output_frames_dir, 'kde_construction_convolution_{i:0{width}}.png')

    for i, x0 in enumerate(x_grid):
        plot_kernel_contribution(data, x0, epa_kernel)
        plt.plot(x_grid[:(i+1)], y_grid[:(i+1)], '-', color='k')
        plt.savefig(fn_format.format(i=i, width=num_zeros))
        plt.clf()


def plot_kernel_contribution(data, point, kernel=epa_kernel):
    plt.plot(data, [0] * len(data), 'o', color=palette[0])

    x_grid = np.linspace(point - 1, point + 1, 1000)
    y_grid = kernel(x_grid, point)
    plt.plot(x_grid, y_grid, '-', color=palette[1], alpha=0.5)

    nonzero_points = [(x, kernel(x, point)) for x in data if kernel(x, point) > 0]
    for x, y in nonzero_points:
        plt.plot((x,x), (0,y), '--', color=palette[0])
        plt.plot(x, y, 'o', color=palette[1])

    plt.xlabel('$x$')
    plt.ylabel(r'$\rho(x)$')

    plt.xlim(min(data) - 1.1, max(data) + 1.1)
    plt.ylim(-0.025, 0.85)
    sns.despine()


def inverted_plot_contribution(data, x_grid, kernel=epa_kernel):
    plt.plot(data, np.zeros(data.shape), 'o', color=palette[0])
    for x in data:
        plt.plot(x_grid, kernel(x_grid, x), color=palette[1])

    plt.plot(x_grid, kde(data, x_grid, kernel), 'k')
    plt.xlabel('$x$')
    plt.ylabel(r'$\rho(x)$')

    plt.xlim(min(data) - 1.1, max(data) + 1.1)
    plt.ylim(-0.025, 0.85)
    sns.despine()
    plt.savefig('kde_construction_inverted.svg')

    plt.clf()
