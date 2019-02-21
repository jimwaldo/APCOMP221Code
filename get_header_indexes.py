#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-21

@author waldo

Reads the first line of a csv file, and produces a csv file where each line has two columns; the first is the index
of the column in the input csv, and the second is the header for that column. Useful when looking at a large csv file
with an unknown set of columns.
"""

import sys, csv

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python get_header_indexes.py infile.csv outfile.csv')
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    cin = csv.reader(fin)

    fout = open(sys.argv[2], 'w')
    cout = csv.writer(fout)

    h = next(cin)
    fin.close()

    for i in range(0, len(h)):
        cout.writerow([i, h[i]])

    fout.close()