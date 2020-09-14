'''
Data Analysis
CIS 210 F18 Project 6-2

Author: Hans Prieto
Credits: [N/A]

Understand, impement, and revise
data analysis and visualization
functions

Practice with
- data analysis
- Python collections: lists and dictionaries
'''

import doctest

def mean(alist):
    '''
    (list) -> float

    returns the mean of a list of
    numbers

    >>> mean([1, 1, 2, 3, 4, 5])
    2.6666666666666665

    >>> mean([1, 2, 3, 3, 3, 4, 5])
    3.0

    >>> mean([1, 2, 3, 4])
    2.5
    '''
    
    mean = sum(alist) / len(alist)
    return mean
    
def isEven(n):
    '''
    (int) -> boolean

    determines whether or not a number
    is even

    >>> isEven(3)
    False

    >>> isEven(4)
    True

    >>> isEven(6)
    True
    '''
    
    if n % 2 == 0:
        return True
    else:
        return False
    
def median(alist):
    '''
    (list) -> number

    returns the mediann of a list
    of numbers

    >>> median([1, 1, 2, 3, 4, 5])
    2.5

    >>> median([1, 1, 2, 3, 4])
    2

    >>> median([1, 2, 4, 4])
    3.0
    '''
    
    copylist = alist[:] #make a copy using slice operator
    copylist.sort()
    if isEven(len(copylist)): #evenLength
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid])/2
    else:       #odd length
        mid = len(copylist)//2
        median = copylist[mid]
    return median
    
def genFrequencyTable(alist):
    '''
    (list) -> dictionary

    generates the dictionary of frequency
    counts from a list of numbers

    >>> genFrequencyTable([1, 2, 3, 3, 1, 4, 5])
    {1: 2, 2: 1, 3: 2, 4: 1, 5: 1}

    >>> genFrequencyTable([1, 2, 3, 4, 4, 5])
    {1: 1, 2: 1, 3: 1, 4: 2, 5: 1}
    '''
    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1

    return countdict
    
def mode(alist):
    '''
    (list) -> number

    returns the mode from a list of
    numbers

    >>> mode([1, 2, 3, 4, 4])
    [4]

    >>> mode([1, 2, 2, 2, 3, 3, 3, 4])
    [2, 3]

    >>> mode([1, 2, 3, 3])
    [3]
    '''
    
    countdict = genFrequencyTable(alist)

    countlist = countdict.values()
    maxcount = max(countlist)

    modelist = []
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)

    return modelist
    
def frequencyTable(alist):
    '''
    (list) -> frequencyTable

    returns a frequency table for
    a list of numbers.

    > frequencyTable([1, 3, 3, 2])
    ITEM   FREQUENCY
    1      1
    2      1
    3      2

    > frequencyTable([1, 3, 3, 3, 2])
    ITEM   FREQUENCY
    1      1
    2      1
    3      3
    '''
    countdict = genFrequencyTable(alist)

    itemlist = list(countdict.keys())
    itemlist.sort()

    print("ITEM","FREQUENCY")

    for item in itemlist:
        print(item, "   ", countdict[item])
    
def main():
    equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
    2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
    4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
    4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
    2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
    4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
    3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
    2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
    2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
    6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
    2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
    2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
    4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
    4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
    2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
    2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
    2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
    4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
    4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
    2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
    3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
    2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
    2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
    2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
    2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
    2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
    3.1, 4.6, 2.8, 3.1, 6.3]

    frequencyTable(equakes)
    
    print('mean is', mean(equakes))

    print('median is ', median(equakes))

    print('mode is ', mode(equakes))

doctest.testmod()
main()

    


