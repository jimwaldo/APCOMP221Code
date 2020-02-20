#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18

@author waldo
Get a random sample of lines of a specified size from a csv file, and write those lines a random
number of times, up to 25, to a new
file. The output file may not include as many lines as specified if the original file is exhausted
before the maximum number is reached. Currently this picks about 1 out of every 10 lines.
"""

import random, sys, csv

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python randomSample.py from_file to_file sample_size')
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    csv_in = csv.reader(fin)

    fout = open(sys.argv[2], 'w')
    csv_out = csv.writer(fout)

    end_count = int(sys.argv[3])

    h = next(csv_in)
    csv_out.writerow(h)

    i = 0
    for l in csv_in:
        if (random.randint(1,10) == 7):
            l.remove(l[2])
            n = random.randint(1,25)
            j = 0
            while j < n:
                csv_out.writerow(l)
                j += 1
            i += 1
        if i >= end_count:
            break

    fin.close()
    fout.close()