'''                          # FILE HEADER
Approximate Square Root
CIS 210 F18 Project 2

Author: Hans Prieto

Credits: [N/A]

Approximate the square root of a number using
iterative algorithm; compare result of this algorithm
to Python square root function result. 
'''

import math
def mysqrt(n, k):
    ''' (integer, integer) -> float

        Generates an approximate square root for n,
        a positive integer, via an interactive process
        that runs k times.
        The approximate square root is returned.
        
                    #Examples of Use
        >>> mysqrt(1, 1)
        1.0
        >>> mysqrt(4, 1)
        2.5
        >>> mysqrt(4, 2)
        2.05
    '''
    result = 1
    for i in range(k):
        result = 0.5 * (result + n/result)
    return result

def sqrt_compare(n, k):
    ''' (integer, integer) -> print

        Generates an approximate square root for n,
        a positive integer, via an interactive process
        that runs k times.
        The approximate square root is returned.
        
                    #Examples of Use
        >>> sqrt_compare(10000, 8)
        For 10000 using 8 iterations: 
        mysqrt value is:  101.20218365353946
        math lib sqrt value is:  100.0
        This is a 1.2 percent error.

        >>> sqrt_compare(10000, 9)
        For 10000 using 9 iterations: 
        mysqrt value is:  100.00714038711746
        math lib sqrt value is:  100.0
        This is a 0.01 percent error.
        
        >>> sqrt_compare(25, 5)
        For 25 using 5 iterations: 
        mysqrt value is:  5.000023178253949
        math lib sqrt value is:  5.0
        This is a 0.0 percent error.
    '''
    print("For " + str(n) + " using " + str(k) + " iterations: ")
    print("mysqrt value is: ", mysqrt(n, k))
    print("math lib sqrt value is: ", math.sqrt(n))
    percent_error = round(abs((mysqrt(n, k) - math.sqrt(n))/math.sqrt(n) * 100), 2)
    print("This is a " + str(percent_error) + " percent error.")

def main():
    '''Square root comparison program driver.
        Compares the approximate square root of
        a number to the actual square root of
        that number
    '''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(100, 10)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None

main()






