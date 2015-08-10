#! /usr/bin/env python
import argparse
import screed

parser = argparse.ArgumentParser()
parser.add_argument('readsfile')
parser.add_argument('distfile')
parser.add_argument('target_cov', type=int)

args = parser.parse_args()

# get average readlen
sumlen = 0
for n, record in enumerate(screed.open(args.readsfile)):
    if n >= 1000:
        break
    sumlen += len(record.sequence)

avglen = sumlen / float(n)

# print avglen, sumlen, n

###

start = args.target_cov / 2.
stop = args.target_cov * 2.
repeat_start = args.target_cov * 5.

sum_reads = 0.
sum_cov = 0.
n_cov = 0.

sum_repeat_cov = 0.

first = True
for line in open(args.distfile):
    if first:                           # skip first row
        first = False
        continue

    cov, count = line.split(',')[:2]
    cov = int(cov)
    count = int(count)

    # average coverage is estimated by looking at single-copy peak
    if cov >= start and cov <= stop:
        sum_cov += (cov * count)
        n_cov += count

    # genome size is estimated by looking at coverage-adjusted read count
    if cov >= start:
        adj_count = float(count) / float(cov)
        sum_reads += adj_count

    # repeat content can be estimated by looking at any given slice.
    if cov >= repeat_start:
        adj_count = float(count) / float(cov)
        sum_repeat_cov += adj_count

print 'Estimated total genome size is: %d bp' % (sum_reads * avglen)
print 'Estimated size > 5x repeats is: %d bp' % (sum_repeat_cov * avglen)
print 'Estimated single-genome coverage is: %.1f' % (sum_cov / n_cov)
