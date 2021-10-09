#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:41:23 2020

@author: xg7
"""
#s = input()


def fun1(c, s):
   total = 0 
   for i in s:
       if i == c:
           total += 1
   return total
       


if __name__ == "__main__":
    print(fun1('l', 'hello'))
    print(fun1('z', 'hello'))


