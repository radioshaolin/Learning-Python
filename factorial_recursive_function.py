#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-06-22 22:33:24
# @Last Modified by:   shaolinfm
# @Last Modified time: 2015-06-25 17:04:03

def factorial_recursion(n):
    '''
        This is example of using recursion inside function for calculating factorial for N
    '''
    try:
        n = abs(int(n))
        if n == 0:
            return 1
        else:
            return n * factorial_recursion(n-1)

    except Exception as e:
        print "Unexpected error:", type(e), e

def run_tests():
    '''Run testcases for the factorial_recursion method.'''
    import math
    assert(factorial_recursion(100) == math.factorial(100))

if __name__ == "__main__":
    run_tests()
