import math

def year(l, p, a):
    i = (l * 0.01 / 12)
    num = pow(1 + i, p)

    return a * ((i * num) / (num - 1))


def a(l, q, p):
    i = (l * 0.01 / 12)
    num = pow(1 + i, p)

    return q / ((i * num) / (num - 1))


def t(l, m, a):
    i = (l * 0.01 / 12)
    A = (m / (m - i * a))

    return math.ceil(math.log(A, i + 1))


def n():
    a = int(input('Enter the loan principal: '))
    payment = int(input('Enter the monthly payment: '))
    a_interest = int(input('Enter the loan interest: '))

    n = t(a_interest, payment, a)

    years = n / 12
    month = (years - math.floor(years)) * 12
    print('It will take {} years and {} months to repay this loan!'.format(math.floor(years), math.floor(month)))


def ab():
    a = int(input('Enter the loan principal: '))
    periods = int(input('Enter the number of periods: '))
    a_interest = int(input('Enter the loan interest: '))

    payment = math.ceil(year(a_interest, periods, a))

    print('Your monthly payment = {}!'.format(payment))


def p():
    annuity_payment = float(input('Enter the annuity payment: '))
    periods = int(input('Enter the number of periods: '))
    a_interest = float(input('Enter the loan interest: '))

    principal = math.floor(a(a_interest, annuity_payment, periods))

    print('Your loan principal = {}!'.format(principal))



def CreditCalculator():
    z = input('What do you want to calculate?\ntype "n" for number of monthly payments,\ntype "a" for annuity monthly payment amount,\ntype "p" for loan principal:')


    if z == 'n':
        n()
    elif z == 'a':
        ab()
    elif z == 'p':
        p()


CreditCalculator()