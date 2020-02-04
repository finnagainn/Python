#-------------------------------------------------------------------------------
# Name:        Tip Tax Total
# Purpose:     calculate the cost of a meal
#
# Author:      Kaffeein Bellamy
#
# Created:     Sept 4, 2018
#
#-------------------------------------------------------------------------------

meal_price = float(input('Enter the price of the meal '))
lone_tip = 0.18
lone_tax = 0.07
ind_tip = (float(lone_tip) * float(meal_price))
ind_tax = (float(lone_tax) * float(meal_price))
total = float(meal_price) + float(lone_tip) + float(lone_tax)

print('Your tip is $', format(ind_tip, '.2f'))
print('Your sales tax is $', format(ind_tax, '.2f'))
print('Your total meal costs $', format(total, '.2f'))