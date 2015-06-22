#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-06-22 22:33:24
# @Last Modified by:   Ivan Zemlyaniy
# @Last Modified time: 2015-06-23 00:26:00

def fibonacci_sequence(n):
    '''
        Recursive function of Fibonacci sequence
    '''
    try:
        def recur_fibo(n):
            if n <= 1:
                return n
            else:
                return(recur_fibo(n-1) + recur_fibo(n-2))

        # check if the number of terms is valid
        if n <= 0:
            print("Plese enter a positive integer")

        # executin of recur_fibo function
        else:
            return [recur_fibo(i) for i in range(n)]


    except Exception as e:
        print "Unexpected error:", type(e), e

def run_tests():
    '''Run testcases for the fibonacci_sequence method.'''
    assert(fibonacci_sequence(2) == [0, 1])
    assert(fibonacci_sequence(8) == [0, 1, 1, 2, 3, 5, 8, 13])
    assert(fibonacci_sequence(24) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657])

if __name__ == "__main__":
    run_tests()

