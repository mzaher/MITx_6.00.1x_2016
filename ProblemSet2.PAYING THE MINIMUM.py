totalPaid = 0
monthlyInterestRate = annualInterestRate / 12.0
for month in range(0, 12):
    minMonhtlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMonhtlyPayment
    totalPaid += minMonhtlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    month += 1
    print('Month: %s' % month)
    print('Minimum monthly payment: %s' % (round(minMonhtlyPayment, 2)))
    print('Remaining balance: %s' % (round(balance, 2)))
print('Total paid: %s' % (round(totalPaid, 2)))
print('Remaining balance: %s' % str(round(balance, 2)))
