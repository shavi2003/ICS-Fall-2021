#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:48:42 2021

@author: bing
"""
def fraction2binary(f, space):
    ##complete the code
    b = ''
    while f != 0:
        f *= 2
        if f >= 1:
            f -= 1
            b += '1'
        else:
            b += '0'
    if space >= len(b):
        b += '0' * (space - len(b))
    else:
        b = b[:space]
    
    
    return '0.'+b


def binary2fraction(b):
    ##complete the code
    b = b[2:]
    fraction = 0
    counter = -1
    for i in b:
        fraction += int(i) * (2 ** counter)
        counter -= 1
    return fraction
    
    

if __name__ =='__main__':
    print('2.07 - 2 =', 2.07 - 2)
    f = 0.07
    l = 52
    print('The binary of 0.07 in your machine:')
    print(fraction2binary(f, l))
    print('Influence of the Truncation error')
    print(binary2fraction(fraction2binary(f, l)))
