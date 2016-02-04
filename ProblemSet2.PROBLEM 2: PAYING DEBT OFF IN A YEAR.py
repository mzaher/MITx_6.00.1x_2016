monthlyInterestRate = annualInterestRate / 12.0
monthlyFixedPayment = 0
newBalance = balance
while newBalance > 0:
    newBalance = balance
    monthlyFixedPayment += 10
    for month in range(12):
        newBalance = newBalance - monthlyFixedPayment
        newBalance *= 1 + monthlyInterestRate
print("Lowest payment: %s" % monthlyFixedPayment)
