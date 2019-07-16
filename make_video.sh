#!/bin/sh
ffmpeg -r 16 -i kde_construction_convolution_%03d.png -vcodec libvpx kde_construction_convolution.webm

convert -delay 6 *.png kde_construction_convolution.gif