balance = 3329

annualInterestRate = 0.2

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


min_monthly_pay = 10
while True:
    final_balance = get_balance(balance, min_monthly_pay)
    if final_balance > 0:
        min_monthly_pay += 10
    else:
        print "Lowest Payment: " + str(min_monthly_pay)
        break
