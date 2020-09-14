'''
CIS 210 Fall 2018 Project 9-1

Author: Hsns Prieto

Credits: N/A

Design, implement, and test
recursive and iterative algorithms
for determining sequence inclusion
using binary search.
'''

def isMemberR(aseq, target):
    '''
    (sequence, object) -> boolean

    Uses a recursive approach to
    implement a binary search algorithm
    to determine whether a given element
    (target) is a member of a given sequence
    (aseq)

    >>> isMemberR((23, 24, 25, 26, 27), 25)
    True

    >>> isMemberR((42,), 42)
    True

    >>> isMemberR((), 99)
    False
    '''
    if len(aseq) == 0:
        return False
    else:
        mid = len(aseq) // 2

        if aseq[mid] == target:
            return True
        elif aseq[mid] > target:
            return(isMemberR(aseq[:mid], target))
        else:
            return(isMemberR(aseq[mid+1:], target))
        
def isMemberI(aseq, target):
    '''
    (sequence, object) -> boolean

    Uses an iterative approach to
    implement a binary search algorithm
    to determine whether a given element
    (target) is a member of a given sequence
    (aseq)

    >>> isMemberI((1, 2, 3, 3, 4), 4)
    True

    >>> isMemberI('aeiou', 'y')
    False

    >>> isMemberI((), 99)
    False
    '''
    first = 0
    last = len(aseq) - 1
    
    while first <= last:
        mid = (first + last) // 2
        if aseq[mid] == target:
            return True
        elif aseq[mid] > target:
            last = mid - 1
        else:
            first = mid + 1

    return False

def bintest(f):
    '''
    (function) -> None

    Test function f (one of
    the binary search functions).
    Report results for each test.

    > bintest(isMemberR)
    <report result>
    > bintest(isMemberI)
    <report results>
    '''
    
    test_cases = (
        ((1, 2, 3, 3, 4), 4, True),
        ((1, 2, 3, 3, 4), 2, True),
        ('aeiou', 'i', True),
        ('aeiou', 'y', False),
        ((1, 3, 5, 7), 4, False),
        ((23, 24, 25, 26, 27), 5, False),
        ((0, 1, 4, 5, 6, 8), 4, True),
        ((0, 1, 2, 3, 4, 5, 6), 3, True),
        ((1, 3), 1, True),
        ((2, 10), 10, True),
        ((99, 100), 101, False),
        ((42,), 42, True),
        ((43,), 44, False),
        ((), 99, False),
        )

    for test in test_cases:
        #pass the arguments
        arg1 = test[0]
        arg2 = test[1]
        expected_result = test[2]

        #report test case
        print(f"Checking {f.__name__}({arg1}, {arg2})...", end='')

        #execute the test
        actual_result = f(arg1, arg2)

        #report result
        if (actual_result == expected_result):
            print(f"its value {actual_result} is correct!")
        else:
            print("Error: has wrong value {}, expected {}.".format(actual_result, expected_result))

    return None

def main():
        '''calls binary search test function 2 times'''
        bintest(isMemberR)
        print()
        bintest(isMemberI)
        return None

if __name__ == '__main__':
    main()
    
