balance = 999999


annualInterestRate = 0.18


def get_balance(balance, min_monthly_pay):
    month = 1
    while True:
        if month < 13:
            unpaid_monthly_balance = balance - min_monthly_pay
            monthly_interest = unpaid_monthly_balance * annualInterestRate/12
            balance = unpaid_monthly_balance + monthly_interest
            month += 1
        else:
            final_balance = balance
            break
    return final_balance

# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

low = balance/12
high = balance * (1+ annualInterestRate/12)**12 * 1/12

min_monthly_pay = 1/2*(high -low)
while True:
    final_balance = get_balance(balance, min_monthly_pay)
    if final_balance > 0:
        low = min_monthly_pay
        high = high
        min_monthly_pay = low + (high -low)/2
    ## because the way computer represents decimals, never get to 0
    ## rather use a number very close to 0
    elif final_balance < -0.0001:
        low = low
        high = min_monthly_pay
        min_monthly_pay = low + (high-low)/2
    else:
        print "Lowest Payment: " + str(round(min_monthly_pay,2))
        break
