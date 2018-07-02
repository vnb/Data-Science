#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:19:17 2018

@author: varshabhat
"""

import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    even_no = [x for x in range(0,100,2)]
    len_list = len(even_no)
    rand_index = random.randint(0, len_list-1)
    return even_no[rand_index]
print(genEven())