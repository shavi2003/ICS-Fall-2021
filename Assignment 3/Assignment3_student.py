#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:12:38 2017

@author: xg7
"""

# Q1
def order(p, q, n):
    
    if n >= len(p) or n >= len(q):
        return -1
    if p[n] > q[n]:
        return True
    else:
        return False
    
    



# Q2
def first_max(order_f, l, n):
    
    temp = 0
    a = l[temp]
    while temp < len(l):
        if not order_f(a, l[temp], n) and a[n] != l[temp][n]:
            a = l[temp]
        temp += 1
    return a
            
    
            
        
        
        
    


# Q3 
def last_max(order_f, l, n):
    
    temp = 0
    a = l[temp]
    while temp < len(l):
        if not order_f(a, l[temp], n):
            a = l[temp]
        temp += 1
    return a


##testing part. 
##You code should pass the tests and give the correst outputs.
##You can comment out them temporarily if you want. 
if __name__ == "__main__":
    print("---testing---")
    result = order((1, 2, 3), (2, 1, 4), 0)
    print("order((1, 2, 3), (2, 1, 4), 0) returns:", result)
    result = order((1, 2, 3), (2, 1, 4), 1)
    print("order((1, 2, 3), (2, 1, 4), 1) returns:", result)
    result = order((1, 2, 3), (2, 1, 4), 2)
    print("order((1, 2, 3), (2, 1, 4), 2) returns:", result)
    t = [('X', 5), ('B', 6), ('P', 4), ('X', 3), ('B', 5),('P', 6)]
    print("t =", t)
    print("first_max(order, t, 1) returns:")
    print(first_max(order, t, 1))
    print("Bonus: last_max(order, t, 1) returns:")
    print(last_max(order, t, 1))
    