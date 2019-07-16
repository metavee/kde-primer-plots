# kde-primer-plots
Code for generating the plots in my [KDE primer](https://metavee.github.io/blog/technical/2017/11/25/kernel-density-estimation-primer.html).

## Setup

Should run in both Python 2 and Python 3.

See `requirements.txt` for the required dependencies and install with `pip install -r requirements.txt`. You may wish to do so in a [`virtualenv`](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) (or [`conda env`](https://conda.io/docs/user-guide/tasks/manage-environments.html) if you're using Anaconda).

## Running the code

Run `python make_plots.py`, and inspect the output in the `plots/` subdirectory. If you have [FFMPEG](https://www.ffmpeg.org/) or [ImageMagick](https://www.imagemagick.org/script/index.php), the script `make_video.sh` can be run from inside `plots/kde_construction_convolution/` to generate the videos.
