#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:48:59 2020

@author: xg7
"""

import string

def lenLastWord(s):
    for i in s:
        if i in string.punctuation:
            s = s.replace(i, '')
            
    word_list = s.split()
    return len(word_list[-1])
            



##test
if __name__ == "__main__":
    
    s = "hello world."
    print(lenLastWord(s))
    
    s = "Good morning  !"
    print(lenLastWord(s))
   
