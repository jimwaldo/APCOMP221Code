#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
"""
Created on 2/16/20

@author waldo

"""

import sys, csv, hashlib

def build_dict(csv_in):
    ret_dict = {}

    for l in csv_in:
        l.remove(l[1]) #The student id
        qi_s = ''.join(l)
        ret_dict[qi_s] = ret_dict.setdefault(qi_s, 0) + 1

    return ret_dict


def build_dict2(csv_in):
    ret_dict = {}

    for l in csv_in:
        m = hashlib.md5()
        l.remove(l[1])
        m.update(bytes(''.join(l), 'utf-8'))
        h = m.hexdigest()
        ret_dict[h] = ret_dict.setdefault(h,0) + 1

    return ret_dict

def build_k_dict(qi_d):
    k_d = {}

    for v in qi_d.values():
        k_d[v] = k_d.setdefault(v,0) + 1
    return k_d

def build_k_list(count_d):
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




