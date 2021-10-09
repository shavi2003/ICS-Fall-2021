#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:43:58 2020

@author: xg7
"""

def camel2snake():
    camel = input('Please input a camel: ')
    camel_plagiate = ''
    for i in camel:
        if i.isupper():
            camel_plagiate += '_' + i.lower()
        else:
            camel_plagiate += i
            
    return camel_plagiate
    
            
            




print(camel2snake())