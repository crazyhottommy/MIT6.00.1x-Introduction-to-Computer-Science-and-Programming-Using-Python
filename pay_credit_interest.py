## For each month:
## Compute the monthly payment, based on the previous month’s balance.
## Update the outstanding balance by removing the payment, then charging interest on the result.
## Output the month, the minimum monthly payment and the remaining balance.
## Keep track of the total amount of paid over all the past months so far.
## Print out the result statement with the total amount paid and the remaining balance.

balance = 4842

annualInterestRate = 0.2

monthlyPaymentRate = 0.04

month = 1
total_paid = 0
while True:
    if month < 13:
        min_monthly_pay = balance * monthlyPaymentRate
        unpaid_monthly_balance = balance - min_monthly_pay
        monthly_interest = unpaid_monthly_balance * annualInterestRate/12
        balance = unpaid_monthly_balance + monthly_interest
        print "Month: " + str(month)
        print "Minimum monthly payment: " + str(round(min_monthly_pay,2))
        print "Remaining balace: " + str(round(balance,2))
        total_paid += min_monthly_pay
        month += 1
    else:
        break
print "Total_paid: " + str(round(total_paid,2))
print "Remaining balance: " + str(round(balance,2))

