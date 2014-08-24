#! /usr/bin/env python
import sys
from matplotlib.pylab import *
import numpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--xmin', type=int, default=None)
parser.add_argument('--xmax', type=int, default=None)
parser.add_argument('--ymin', type=int, default=None)
parser.add_argument('--ymax', type=int, default=None)
parser.add_argument('dist_file')
parser.add_argument('image_output')

args = parser.parse_args()

x = numpy.loadtxt(args.dist_file)
plot(x[:, 0], x[:, 1])
xlabel('k-mer coverage')
ylabel('# of reads with that coverage')
title('read coverage spectrum: %s' % args.dist_file)
axis(xmin=args.xmin, ymin=args.ymin, xmax=args.xmax, ymax=args.ymax)
savefig(args.image_output)
