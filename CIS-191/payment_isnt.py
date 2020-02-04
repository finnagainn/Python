#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kaffeein  Bellamy
#
# Created:     04/09/2018
# Copyright:   (c) CIS 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

purch_amt = float(input('Enter purchase amount '))
pymt_inst = int(input('Enter desired number of installments '))
rate = 0.05

total = (float(rate) * float(purch_amt)) + float(purch_amt)
sing_inst = (total / pymt_inst)

print('The total amount is ', total)
print('Each individual installment will be ', sing_inst)