#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 16:27:15 2018

@author: waldo
"""

import csv, sys

def clean_file(csv_in, csv_out):
    total_lines = 0
    good_lines = 0
    bad_lines = 0

    header = next(csv_in)
    l_len = len(header)
    while True:
        try:
            total_lines += 1
            l = next(csv_in)
            if len(l) == len(l_len):
                csv_out.writerow(l)
                good_lines += 1
            else:
                bad_lines += 1
        except StopIteration:
            total_lines -= 1
            break
        except:
            bad_lines += 1
            continue
    return total_lines, good_lines, bad_lines

def clean_csv(fin_n, fout_n):
    '''
    Read a .csv file and create a new .csv file that contains all the lines that
    do not throw an exception when attempting to read. Useful for cleaning out
    unreadable characters and other transfer flaws.
    :param fin_n: The name of the .csv file to be cleaned
    :param fout_n: The name of the .csv file the is the result of the cleaning
    '''
    fin = open(fin_n, 'r')
    cin = csv.reader(fin)
    
    fout = open(fout_n, 'w')
    cout = csv.writer(fout)
    total_lines, good_lines, bad_lines = clean_csv(cin, cout)
    fout.close()
    fin.close()
    print('Total lines = ' + str(total_lines), 'Good lines = ' + str(good_lines),
          'Bad lines = ' + str(bad_lines))
    return None

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python clean_csv.py file_to_clean.csv cleaned_file.csv')
        sys.exit(1)

    name_in = sys.argv[1]
    name_out = sys.argv[2]
    clean_csv(name_in, name_out)