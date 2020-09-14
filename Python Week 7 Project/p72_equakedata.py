'''
Earthquake Watch
CIS 210 F18 Project 7-2

Author: Hans Prieto
Credits: [N/A]

Use file processing and data analysis to find
and report information about earthquake activity
centered in Eugene, Oregon, over the past 100
years

Practice with
- data analysis and file processing
'''

import p62_data_analysis as p62
import doctest

def equake_readf(fname):
    '''
    (str) -> list

    Opens file fname, and creates and returns
    a list of the earthquake magnitudes from
    this file

    >>> equake_readf('equakes50f.txt')
    [5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0, 5.2, 5.1, 5.4, 5.2, 5.6]

    >>> equake_readf('equakes_short.txt')
    [2.99, 2.56, 2.83, 2.76]
    '''
    with open(fname, 'r') as equakefile:
        datali = equakefile.readlines()
        magnitudes = []
        for line in datali[1:]:
            values = line.split(',')
            magnitudes.append(float(values[4]))
    
        return magnitudes

def equake_analysis(magnitudes):
    '''
    (list) -> tuple
    
    Returns the mean, median, and mode
    from a list of earthquake magnitudes.

    >>> equake_analysis([2.99, 2.56, 2.83, 2.76])
    (2.785, 2.795, [2.99, 2.56, 2.83, 2.76])

    >>> equake_analysis([5.0, 5.2, 5.1, 5.4, 5.2, 5.6, 5.6])
    (5.3, 5.2, [5.2, 5.6])
    
    >>> equake_analysis([5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0])
    (5.437500000000001, 5.4, [5.0])
    '''
    
    magnitudes_mean = p62.mean(magnitudes)
    magnitudes_median = p62.median(magnitudes)
    magnitudes_mode = p62.mode(magnitudes)

    return magnitudes_mean, magnitudes_median, magnitudes_mode

def equake_report(magnitudes, mmm):
    '''
    (list, tuple) -> None

    Reports the number(count) of earthquakes, and the mean, median,
    and mode of magnitudes.

    Calls the function frequencyTable from project 6-2 to report
    the number of occurences of each item in magnitudes.
    
    >>> equake_report([2.99, 2.56, 2.83, 2.76],(2.785, 2.795, [2.99, 2.56, 2.83, 2.76]))
    There have been 4 earthquakes over the past 25 years
    Mean magnitude is: 2.785
    Median magnitude is: 2.795
    Mode(s) of magnitude is: [2.99, 2.56, 2.83, 2.76]
    ITEM FREQUENCY
    2.56     1
    2.76     1
    2.83     1
    2.99     1

    >>> equake_report([5.0, 5.2, 5.1, 5.4, 5.2, 5.6, 5.6],(5.3, 5.2, [5.2, 5.6]))
    There have been 7 earthquakes over the past 25 years
    Mean magnitude is: 5.3
    Median magnitude is: 5.2
    Mode(s) of magnitude is: [5.2, 5.6]
    ITEM FREQUENCY
    5.0     1
    5.1     1
    5.2     2
    5.4     1
    5.6     2

    >>> equake_report([5.2, 5.1, 6.0, 5.9, 5.6, 5.7, 5.0, 5.0],(5.437500000000001, 5.4, [5.0]))
    There have been 8 earthquakes over the past 25 years
    Mean magnitude is: 5.437500000000001
    Median magnitude is: 5.4
    Mode(s) of magnitude is: [5.0]
    ITEM FREQUENCY
    5.0     2
    5.1     1
    5.2     1
    5.6     1
    5.7     1
    5.9     1
    6.0     1
    '''
    
    magnitudes_mean = mmm[0]
    magnitudes_median = mmm[1]
    magnitudes_mode = mmm[2]
    num_equakes = len(magnitudes)

    print('There have been', num_equakes, 'earthquakes over the past 25 years')
    print('Mean magnitude is:', magnitudes_mean)
    print('Median magnitude is:', magnitudes_median)
    print('Mode(s) of magnitude is:', magnitudes_mode)

    p62.frequencyTable(magnitudes)
    
    return None

def main():
    '''()-> None
    Calls: equake_readf, equake_analysis, equake_report
    Top level function for earthquake data analysis.
    Returns None.
    '''
    #fname = 'equakes25f.txt'
    fname = 'equakes50f.txt'
    #fname = 'equakes_short.txt'

    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(emags, mmm)
    return None


#doctest.testmod()
main()
