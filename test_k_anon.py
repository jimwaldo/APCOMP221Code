#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2/16/20

@author waldo

Test a csv file for k-anonymity. The assumption is that the csv file has as its first entry an identifier, and
then a list of quasi-identifiers. This program will build a dictionary keyed by the concatenation of the quasi-identifiers,
with value the number of entries in the dataset that have that combination of quasi-identifiers. The program will print
a list of k-anon values and the number of records that have that level of k-anonymity. It will also write a .csv file
with this information.

"""

import sys, csv, hashlib

def build_dict(csv_in):
    """
    Build a dictionary keyed by the quasi-identifiers with value the count of the number of records with that set of
    quasi-identifiers. The csv passed in should have the header information removed.
    :param csv_in: an open csv reader with the header already read, with first field an id and other fields the quasi-
    identifiers
    :return: a dictionary keyed by the concatenation of the quasi-identifers and value the count of the number of records
    with that set of quasi-identifiers
    """
    ret_dict = {}

    for l in csv_in:
        # concatenate all of the quasi-identifiers, leaving out the user id
        qi_s = ''.join(l[1:])
        ret_dict[qi_s] = ret_dict.setdefault(qi_s, 0) + 1

    return ret_dict


def build_dict2(csv_in):
    """
    Builds a dictionary like that built by build_dict, but with the concatenation of the quasi-identifiers hashed with an
    MD5 hash. Added to allow testing which technique is faster (the un-hashed version is about 10% faster)
    :param csv_in: an open csv reader with the header already read, with first field an id and other fields the quasi-
    identifiers
    :return: a dictionary keyed by the concatenation of the quasi-identifers and value the count of the number of records
    with that set of quasi-identifiers
    """
    ret_dict = {}

    for l in csv_in:
        m = hashlib.md5()
        m.update(bytes(''.join(l[1:]), 'utf-8'))
        h = m.hexdigest()
        ret_dict[h] = ret_dict.setdefault(h,0) + 1

    return ret_dict

def build_k_dict(qi_d):
    """
    Builds a dictionary keyed by level of k-anonymity with values the number of entries that are at that level of
    k-anonymity. Takes as input a dictionary like that built by build_dict, which is keyed by the concatenation of
    quasi-identifiers with values the number of records that have that set of quasi-identifiers.
    :param qi_d: A dictionary keyed by the concatenation of a set of quasi-identifiers and values the number of records
    with that set of values
    :return: A dictionary keyed by the level of k-anonymity with values the number of sets of quasi-identifiers at that
    level
    """
    k_d = {}

    for v in qi_d.values():
        k_d[v] = k_d.setdefault(v,0) + 1
    return k_d

def build_k_list(count_d):
    """
    Builds a list of [k-anonymity level, number of records at that level] from a dictionary like that produced by
    build_k_dict
    :param count_d: A dictionary keyed by k-anonymity level with values the number of quasi-identifier sets that are
    at that level
    :return: a list of lists of the form [k-anonymity level, number of records at that level]
    """
    ret_l = []
    for k,v in count_d.items():
        ret_l.append([k,v])
    ret_l.sort()
    return ret_l


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python test_k_anon.py input_file.csv output_file.csv')
        sys.exit(1)

    fin = open(sys.argv[1], 'r')
    cin = csv.reader(fin)
    h = next(cin)

    k_anon_d = build_dict2(cin)
    fin.close()

    count_d = build_k_dict(k_anon_d)
    k_list = build_k_list(count_d)
    anon_l = [k_list[0][1],k_list[1][1],k_list[2][1],k_list[3][1],0]
    five_a_l = k_list[4:]
    five_anon = 0
    for i in five_a_l:
        five_anon += i[1]
    anon_l[4] = five_anon

    print(anon_l)

    fout = open(sys.argv[2], 'w')
    cout = csv.writer(fout)
    cout.writerow(['K-anon level', 'Count'])
    cout.writerows(k_list)
    fout.close()




