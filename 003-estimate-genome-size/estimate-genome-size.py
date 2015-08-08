#! /usr/bin/env python
import argparse
import screed

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--ksize', type=int, default=20)
parser.add_argument('-C', '--coverage', type=int, default=20)
parser.add_argument('readsfile')
parser.add_argument('report')

args = parser.parse_args()

ksize = args.ksize
coverage = args.coverage

# get average readlen
sumlen = 0
for n, record in enumerate(screed.open(args.readsfile)):
    if n >= 1000:
        break
    sumlen += len(record.sequence) - args.ksize + 1

avglen = sumlen / float(n)

#print avglen, sumlen, n

report_line = open(args.report).readlines()[-1]
n_total_reads = report_line.split(',')[1]
n_total_reads = int(n_total_reads)

print 'Estimated (meta)genome size is: %d bp' % (n_total_reads * avglen / args.coverage,)

