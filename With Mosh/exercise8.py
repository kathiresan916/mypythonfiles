'''price of a house is $1M

If buyer has good credit, 
they need to put down 10%
otherwise
they need to put down 20%
print the down payment'''

price = 1000000

good_credit = False

if good_credit:
    print("Your Downpayment is: ", 0.1 * price)
else:
    print("Your Downpayment is: ", 0.2 * price)

