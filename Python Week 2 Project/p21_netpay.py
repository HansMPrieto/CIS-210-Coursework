'''                          # FILE HEADER
Determining Net Pay
CIS 210 F18 Project 2

Author: Hans Prieto

Credits: [N/A]

Determine the netpay based on the number
of hours worked.
'''

def tax(gross_pay):
    '''int -> float

    Returns tax, based on gross pay.
    The tax rate is 15%, so gross pay
    is multiplied by the tax rate to
    get the amount of tax. 

    >>> tax(107.5)
    16.12
    >>> tax(430)
    64.5
    '''
    
    tax = round(gross_pay * 0.15, 2)
    return tax

def netpay(hours):
    '''int -> float

    Returns netpay, based on the
    number of hours worked.

    >>> netpay(10)
    91.38
    >>> netpay(40)
    365.5
    '''

    hourly_rate = 10.75
    gross_pay = hourly_rate * hours
    netpay = gross_pay - tax(gross_pay)
    return netpay
    
def main():
    '''Net pay program driver.
    Prints the netpay for 10 hours
    of work, and the netpay for 40 hours
    of work.
    '''
    print('For 10 hours work, netpay is: ', netpay(10))
    print('For 40 hours work, netpay is: ', netpay(40))
    return None

main()
