'''                         
Monte Pi (Approximating pi)
CIS 210 F18 Project 3-2
Author: Hans Prieto

Credits: N/A

Approximate pi using the Monte Carlo Algorithm. 
'''

import random
import math

def isInCircle(x, y, r):
    '''(int, int, int) -> Boolean
    
    Returns True if the input
    point (x, y) is inside the circle
    centered at point (0, 0) with radius
    r, and False otherwise.

    >>> isInCirlce(0, 0, 1)
    True
    >>> isInCircle(.5, .5, 1)
    True
    >>> isInCircle(1, 2, 1)
    False
    '''

    d = math.sqrt(x**2 + y**2)
    return(d <= r)
    
def montePi(numDarts):
    ''' (int) -> float

    Returns a random approximate value for pi,
    based on numDarts, which is the number of
    times the approximating pi process should run.

    >>> montePi(100)
    3.08
    >>> montePi(100000)
    3.143072
    >>> montePi(10000000)
    3.1418752
    '''
    inCircle = 0
    for i in range(numDarts):
        x = random.random() #picks a random value for x.
        y = random.random() #picks a random value for y.
        r = 1 #radius of circle is 1
        #the random element means that the examples of function use for montePi may not be replicable.
        
        isInCircle(x, y, r)

        if isInCircle(x, y, r): #determines whether the point (x,y) is in the circle.
            inCircle = inCircle + 1

    pi = inCircle/numDarts * 4 #determines the approximate value of pi.

    return pi #pi value is returned.

def main():
    '''Monte Pi Programming Driver'''
    print(montePi(100))
    print(montePi(1000))
    print(montePi(10000))

main()
        
      


