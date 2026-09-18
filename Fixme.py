#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''

    def is_even(x):
        return x % 2 == 0

    return list(filter(is_even, range(0, n + 1)))
