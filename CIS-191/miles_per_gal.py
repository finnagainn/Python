#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Kaffeein Bellamy
#
# Created:     04/09/2018
# Copyright:   (c) CIS 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

miles_driven = int(input('Enter miles driven'))
gal_used = int(input('Enter gallons used'))
MPG = float(miles_driven / gal_used)

print('Your can travel', MPG, 'miles per gallon')