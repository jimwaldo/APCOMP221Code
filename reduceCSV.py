#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-02-18

@author waldo

Extract a set of columns from a csv file. Takes as input a csv file to read, the csv file to write,
and a configuration file that contains the indexes of the columns to extract from the file being
read and written to the file being written.
"""
import sys, csv
import readConfigFile as rcf

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python reduceCSV.py in_file out_file config_file')
        sys.exit(1)

    keep_fields = rcf.read_int_config_file(sys.argv[3])
    fin = open(sys.argv[1], 'r')
    cin = csv.reader(fin)

    fout = open(sys.argv[2], 'w')
    cout = csv.writer(fout)

    for l in cin:
        out_fields = []
        for i in keep_fields:
            if i < len(l):
                out_fields.append(l[i])
            else:
                break
        cout.writerow(out_fields)

    fin.close()
    fout.close()
