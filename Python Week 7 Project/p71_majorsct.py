'''
Who is in CIS 210?
CIS 210 F18 Project 7-1

Author: Hans Prieto
Credits: [N/A]

Use file processing and data analysis to find
and report information about the range of majors
represented in CIS 210 in Fall 2018

Practice with
- file processing and data analysis
'''

import p62_data_analysis as p62 
import doctest

def majors_readf(fname):
    '''
    (str) -> list

    Opens file fname, and creates and returns
    a list of the majors from this file

    >>> majors_readf('majors_short.txt')
    ['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL']
    '''

    with open(fname, 'r') as majorsfile:
        majors = majorsfile.readline()
        majorsfile.readline()
        mlist = []
        for majors in majorsfile:
            values = majors.split()
            mlist.append(values[0])

    return mlist

def majors_analysis(majorsli):
    '''
    (list) -> tuple

    Determines the most frequently occuring
    major(s) (mode) in a list of majors, and
    also the count of the number of distinct
    majors in the list.

    >>> majors_analysis(['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    (['CIS', 'EXPL'], 3)

    >>> majors_analysis(['CIS', 'EXPL', 'COLT'])
    (['CIS', 'EXPL', 'COLT'], 3)

    >>> majors_analysis(['CIS', 'CIS', 'EXPL', 'COLT'])
    (['CIS'], 3)
    '''
    
    majors_mode = p62.mode(majorsli)

    countdict = p62.genFrequencyTable(majorsli)
    majors_ct = len(countdict)

    return majors_mode, majors_ct

def majors_report(majors_mode, majors_ct, majorsli):
    '''
    (tuple) -> None

    Reports the mode of majorsli and the total
    number of majors represented in the majors list.

    Calls function frequencyTable from project 6-2
    to report the number of occurences of each item in majorsli.

    None value is returned.

    >>> majors_report(['CIS', 'EXPL'], 3, ['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    3 majors are represented in CIS 210 this term.
    The most represented majors(s): CIS, EXPL
    ITEM FREQUENCY
    CIS     2
    COLT     1
    EXPL     2

    >>> majors_report(['CIS', 'EXPL', 'COLT'], 3, (['CIS', 'EXPL', 'COLT']))
    3 majors are represented in CIS 210 this term.
    The most represented majors(s): CIS, EXPL, COLT
    ITEM FREQUENCY
    CIS     1
    COLT     1
    EXPL     1

    >>> majors_report(['CIS'], 3, ['CIS', 'CIS', 'EXPL', 'COLT'])
    3 majors are represented in CIS 210 this term.
    The most represented majors(s): CIS
    ITEM FREQUENCY
    CIS     2
    COLT     1
    EXPL     1
    '''
    
    print(majors_ct, 'majors are represented in CIS 210 this term.')
    majors_mode = ', '.join(majors_mode)
    print('The most represented majors(s):', majors_mode)

    p62.frequencyTable(majorsli)
    
    return None

def main():
    '''()-> None
    Calls: majors_readf, majors_analysis, majors_report
    Top level function for analysis of CIS 210 majors data.
    Returns None.
    > majors_main()
    ''' 
    #fname = 'majors_short.txt'
    fname = 'p71_majors_cis210f18.txt'
    
    majorsli = majors_readf(fname)
    majors_mode, majors_ct = majors_analysis(majorsli)
    majors_report(majors_mode, majors_ct, majorsli)
    
    return None

doctest.testmod()
main()
