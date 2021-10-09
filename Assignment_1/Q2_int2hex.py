#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:09:16 2020

@author: xg7
"""

def int_to_hexa(int_code):
    ##modified the following to the tests
    my_dct = {'0000' : '0', '0001' : '1', '0010' : '2', '0011' : '3', \
              '0100' : '4', '0101' : '5', '0110' : '6', '0111' : '7', \
              '1000' : '8', '1001' : '9', '1010' : 'A', '1011' : 'B', \
              '1100' : 'C', '1101' : 'D', '1110' : 'E', '1111' : 'F'}
    list_a = []
    result = ''
    bin_code = str(bin(int_code))[2:]
    a = ''
    if len(bin_code) % 4 == 1:
        bin_code = '000' + bin_code
    elif len(bin_code) % 4 == 2:
        bin_code = '00' + bin_code
    elif len(bin_code) % 4 == 3:
        bin_code = '0' + bin_code
     
    counter = 0
    for i in bin_code:
        if counter % 4 == 0:
            a += ' '
        a += i
        counter += 1
    
    list_a = a.split()
    
    for i in range(len(list_a)):
        result += my_dct[list_a[i]]
        
      
    return result




##---test of your code, don't change the followings---##
if __name__ == "__main__":
    int_code = 12
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)

    int_code = 16
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)

    int_code = 255
    hexadecimal_code = int_to_hexa(int_code)
    print (int_code, 'converts to', hexadecimal_code)
