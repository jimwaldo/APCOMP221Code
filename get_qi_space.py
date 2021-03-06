#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2/16/20
Will take a file like that produced by reduceCSV.py and will produce a dictionary that maps indexes
to the set of values found at that index, a list of the indexes and the count of different
values for the index, and a csv file that contains the header value of the column and the count of
different values for that column. This assumes that the user_id, used as a key an not a quasi-identifier,
is in the second position (index 1) of the incoming csv, which is a hack but a useful one.

@author waldo

"""

import csv, sys, pickle

def build_range_dict(in_file, qi_count):
    """
    Build a dictionary indexed by the index number of a column with values the set of all different
    values that occur in that column. Will skip the column indexed by 1, which is assumed to be
    the position of the user_id.
    :param in_file: A csv file of the form produced by reduceCSV.py, containing a column for each quasi
    identifier in a data set with the values for that column
    :param qi_count: The number of columns in the dataset
    :return: A dictionary indexed by the index value with value the set of all different values seen at
    that index
    """
    ret_dict = {}
    for l in in_file:
        # we skip the first entry in the line, since that is the user id
        for i in range(1,qi_count):
            ret_dict.setdefault(i, set()).add(l[i])
    return ret_dict

def build_count_list(range_d):
    """
    Takes a dictionary of the form produced by build_range_dict and returns a list of lists. The contained
    list will pair the index value with the count of different values seen for that index. The list is
    sorted from smallest to largest index value
    :param range_d: A dictionary of the form generated by build_range_dict, keyed by column index with values
    the set of values seen at that index
    :return: A list of lists of the form [index, count of distinct values], sorted ascending by index
    """
    count_l = []
    for k,v in range_d.items():
        count_l.append([k,len(v)])
    count_l.sort()
    return count_l

def build_print_list(count_l, head_l):
    """

    :param count_l:
    :param head_l:
    :return:
    """
    ret_l = []
    total = 1
    for p in count_l:
        ret_l.append([head_l[p[0]],p[1]])
        if p[1] != 0:
            total *= p[1]
    ret_l.append(['Total', float(total)])
    return ret_l


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python get_qi_space.py qi_file.csv out_file.csv')
        sys.quit(1)

    fin = open(sys.argv[1], 'r')
    cin = csv.reader(fin)

    h = next(cin)
    i = len(h)
    range_d = build_range_dict(cin, i)
    c_l = build_count_list(range_d)
    fin.close()

    print_l = build_print_list(c_l, h)

    # Now, let's save the various data structures
    fout = open('qi_values.pkl', 'wb')
    pickle.dump(range_d, fout)
    fout.close()
    fout = open('qi_counts.pkl', 'wb')
    pickle.dump(c_l, fout)
    fout.close()
    fout = open(sys.argv[2], 'w')
    cout = csv.writer(fout)
    cout.writerow(['Identifier', 'Count'])
    cout.writerows(print_l)
    fout.close()
