#!/usr/bin/python

import random 
arr =  [x for x in range(1, 11)]   # arr = [1,2,3,4,5,6,7,8,9,10]

random.shuffle(arr) # shuffles sequentially ordered numbers from "arr" array

print(*arr, sep = "\n")
