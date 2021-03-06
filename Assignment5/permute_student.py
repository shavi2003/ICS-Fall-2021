#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:20:57 2021

@author: bing
"""

def permute(nums):
    if len(nums) == 1:
        return [nums]
 
    lst = []
    for i in range(len(nums)):
        rn = nums[:]
        m = rn.pop(i)
        lst.extend([[m] + p for p in permute(rn)])
    return lst

    
##tests

if __name__ == "__main__":
    nums = [1, 2, 3]
    p1 = permute(nums)
    print("Permutation:", p1)
    
    nums = [4, 1, 2, 3]
    p2 = permute(nums)
    print("Permutation:", p2)
    
    nums = [4, 1, 1, 4]
    p3 = permute(nums)
    print("Permutation:", p3)
    

