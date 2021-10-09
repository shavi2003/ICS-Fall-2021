#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Mon Oct  5 22:50:19 2020@author: xg7"""def convert_to_Roman_numeral(n):        m = ["", "M", "MM", "MMM"]    c = ["", "C", "CC", "CCC", "CD", "D",         "DC", "DCC", "DCCC", "CM "]    x = ["", "X", "XX", "XXX", "XL", "L",         "LX", "LXX", "LXXX", "XC"]    i = ["", "I", "II", "III", "IV", "V",         "VI", "VII", "VIII", "IX"]     thousand = m[n // 1000]    hundered = c[(n % 1000) // 100]    ten = x[(n % 100) // 10]    one = i[n % 10]     result = (thousand + hundered +           ten + one)
     
    for i in result:
        if i == ' ':
            result = result.replace(i, '')     return result##testif __name__ == "__main__":    n = 1800    print(convert_to_Roman_numeral(n))


