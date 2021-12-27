import math

def CreditCalculator():
    a = float(input("Enter the loan principal:"))
    b = input("What do you want to calculate? type m – for number of monthly payments,type p – for the monthly payment:")
    if b == "m":
        c = float(input("Enter the monthly payment"))
        months = round(float(a / c))
        print("It will take ", months, " months to repay the loan")
    elif b == "p":
        month = int(input('Enter the number of months: '))
        payment = math.ceil(a / month)
        last = a - (month - 1) * payment
        if payment != last:
          print('Your monthly payment = {} and the last payment = {}'.format(payment, last))
    else:
        print('Your monthly payment = {}'.format(payment))


CreditCalculator()
