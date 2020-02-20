#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2019-03-14

@author waldo

"""

import csv

def find_dups(csv_in, csv_out):
    total_lines = 0
    unique_lines = 0
    dup_lines = 0
    lines_seen = set()

    for l in csv_in:
        total_lines += 1
        key = get_ket(l)
        if key not in lines_seen:
            lines_seen.add(key)
            csv_out.writerow(l)
            unique_lines += 1
        else:
            dup_lines += 1
    return total_lines, unique_lines, dup_lines