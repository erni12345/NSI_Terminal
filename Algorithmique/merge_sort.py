#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:09:59 2021

@author: Guest
"""

import time


def est_trie(t):
    
    for x in range(len(t)-1):
        if t[x] > t[x+1]:
            return False
        
    return True

        


nombre_de_comp = 0

def fusion(t1, t2):
    global nombre_de_comp
    l1 = 0
    l2 = 0
    t = []
    
    while l1 < len(t1) and l2 < len(t2):
        nombre_de_comp += 1
        if t1[l1] >= t2[l2]:
            t.append(t2[l2])
            l2 += 1
        elif t1[l1] <= t2[l2]:
            t.append(t1[l1])
            l1 += 1
        
    
    
    if l1 == len(t1):
        t += t2[l2:]
    
    elif l2 == len(t2):
        t += t1[l1:]
    
    return t





def merge_sort(t):
    
    if len(t) == 1:
        return t
    
    middle = len(t)//2
    
    right = t[middle:]
    left = t[:middle]
    
    right = merge_sort(right)
    left = merge_sort(left)
    
    merged = fusion(right, left)
    
    return merged




import random
start_time = time. time()
merge_sort([random.randint(0,100) for x in range(100000)])
print("--- %s seconds ---" % (time. time() - start_time))
print("le nombre de comp est", nombre_de_comp)


start_time = time. time()
sorted([random.randint(0,100) for x in range(100000)])
print("--- %s seconds ---" % (time. time() - start_time))



        