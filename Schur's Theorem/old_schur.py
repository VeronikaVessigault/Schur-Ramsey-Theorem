from random import SystemRandom
from math import factorial, ceil
from math import e as e

cryto_gen_num = SystemRandom()

import os
import csv 


def get_list_csv(filename):
    file_list = ["keys"]
    if os.path.isfile("{}.csv".format(filename)) and filename in file_list:
        with open('{}.csv'.format(filename)) as csv_file:
            reader = csv.reader(csv_file)
            mylist = list(reader)
            list_tuples = []
            for i in mylist[0]:
                list_tuples.append(eval(i))
            return list_tuples
    return list()


def set_list_csv(filename, mylist):
    file_list = ["keys"]
    if os.path.isfile("{}.csv".format(filename)) and filename in file_list:
        with open('{}.csv'.format(filename), 'w') as csv_file:  
            writer = csv.writer(csv_file)
            writer.writerow(mylist)

def set_keys():
    valid_keys = []

def old_set_keys():
    valid_keys = [] # colorings

    my_list = [(2,j) for j in range(2, ceil(factorial(2)*e))]
    my_list.append((2, ceil(factorial(2)*e)))
    my_list.sort()
    valid_keys.extend(my_list) # 2 coloring, j vertices

    my_list = [(3,j) for j in range(2, ceil(factorial(3)*e))]
    my_list.append((3, ceil(factorial(3)*e)))
    my_list.sort()
    valid_keys.extend(my_list) # 3 coloring

    my_list = [(4,j) for j in range(2, ceil(factorial(4)*e),5)]
    my_list.append((4, ceil(factorial(4)*e)))
    my_list.sort()
    valid_keys.extend(my_list) # 4 coloring

    my_list = [(5,j) for j in range(10, ceil(factorial(5)*e),10)]
    my_list.append((5, ceil(factorial(5)*e)))
    my_list.sort()
    valid_keys.extend(my_list) # 5 coloring

    my_list = [(6,j) for j in range(100, ceil(factorial(6)*e),100)]
    my_list.extend([(6, ceil(factorial(6)*e)), (6, 10), (6, 50)])
    my_list.sort()
    valid_keys.extend(my_list) # 6 coloring

    my_list = [(7,j) for j in range(700, ceil(factorial(7)*e),700)]
    my_list.extend([(7, ceil(factorial(7)*e)), (7, 10), (7, 50), (7, 100), (7, 250), (7, 500)])
    my_list.sort()
    valid_keys.extend(my_list) # 7 coloring

    my_list = [(8,j) for j in range(5000,ceil(factorial(8)*e),5000)]
    my_list.extend([(8, ceil(factorial(8)*e)), (8, 10), (8, 50), (8, 100), (8, 250), (8, 500), (8, 1000), (8, 2500)])
    my_list.sort()
    valid_keys.extend(my_list) # 8 coloring

    my_list = [(9,j) for j in range(15000,ceil(factorial(9)*e),15000)]
    my_list.extend([(9, ceil(factorial(9)*e)), (9, 10), (9, 50), (9, 100), (9, 250), (9, 500), (9, 1000), (9, 2500), (9, 5000), (9, 10000)])
    my_list.sort()
    valid_keys.extend(my_list) # 9 coloring

    my_list = [(10,j) for j in range(50000,ceil(factorial(10)*e),50000)]
    my_list.extend([(10, ceil(factorial(10)*e)), (10, 10), (10, 50), (10, 100), (10, 250), (10, 500), (10, 1000), (10, 2500), (10, 5000), (10,10000), (10, 25000)])
    my_list.sort()
    valid_keys.extend(my_list) # 10 coloring

    set_list_csv("keys", valid_keys)


def run_coloring(n = -1, r = -1, check = False, doubles = False, smallest = True):
    colors = ["red", "blue", "purple", "yellow", "lime", "fuchsia", "orange", "maroon", "cyan", "green"]
    r = 5
    n = ceil(factorial(r)*e)
    parts = {i : list() for i in colors[:r]}
    for i in range(1, n+1):
        rand_num = cryto_gen_num.randrange(r)
        parts[colors[rand_num]].append(i)
    
    smallest = False
    if check:
        check, smallest = check_schur(parts, n, r, doubles, smallest)
    return (parts, check, smallest)

def check_schur(parts = {}, n = -1, r = -1, doubles = False, smallest = True):
    colors = ["red", "blue", "purple", "yellow", "lime", "fuchsia", "orange", "maroon", "cyan", "green"]
    good_schurs = []
    r = 5
    n = ceil(factorial(r)*e)
    
    smallest_num = False
        
    for i in range(0, r):
        my_list = parts[colors[i]]
        list_len = len(my_list)
        for j in range(0, list_len):
            if doubles:
                for k in range(j, list_len):
                    if my_list[j] + my_list[k] in my_list:
                        good_schurs.append((colors[i], my_list[j], my_list[k], my_list[j] + my_list[k]))
            else:
                for k in range(j+1, list_len):
                    if my_list[j] + my_list[k] in my_list:
                        if smallest:
                            if not smallest_num:
                                smallest_num = my_list[j] + my_list[k]
                            elif smallest_num > my_list[j] + my_list[k]:
                                smallest_num = my_list[j] + my_list[k]
                        good_schurs.append((colors[i], my_list[j], my_list[k], my_list[j] + my_list[k]))
    return good_schurs, smallest_num

def run_and_check_many(n = -1, r = -1, runs = 1, doubles = False, smallest = True):
    for i in range(runs):
        parts, good_schurs, smallest_num = run_coloring(n, r, check = True, doubles, smallest)
    
 