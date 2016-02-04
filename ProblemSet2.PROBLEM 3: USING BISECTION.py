monthlyInterestRate = annualInterestRate / 12.0

newBalance = balance
lowerBound = balance / 12.0
higherBound = (balance * ((1.0 + monthlyInterestRate) ** 12)) / 12.0
epsilon = 0.01
minMonthlyPayment = (higherBound + lowerBound) / 2.0


def balanceCalc(balance, minMonthlyPayment, monthlyInterestRate):
	for month in range(12):
		unpaidBalance = balance - minMonthlyPayment
		balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
		month += 1
	return balance


while abs(balance) >= epsilon:
	balance = newBalance
	month = 0
	balance = balanceCalc(balance, minMonthlyPayment, monthlyInterestRate)
	if balance > 0:
		lowerBound = minMonthlyPayment
	else:
		higherBound = minMonthlyPayment
	minMonthlyPayment = (higherBound + lowerBound) / 2.0
print('Lowest Payment: %s' % (round(minMonthlyPayment, 2)))
