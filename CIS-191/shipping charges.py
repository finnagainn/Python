#-------------------------------------------------------------------------------
# Name:        Shipping Charges

# Author:      Kaffeein Bellamy
#
# Created:     Sept 19, 2018
#-------------------------------------------------------------------------------

package_weight = float(input('Please enter package weight in lbs: '))
rate0to2lbs = 1.50 * package_weight #Rate charged for packages weighing 2lbs or less.
rate2to6lbs = 3.00 * package_weight #Rate charged for packages weighing between 2lbs and 6lbs.
rate6to10lbs = 4.00 * package_weight #Rate charged for packages weighing between 6lbs and 10lbs.
rate10lbsplus = 4.75 * package_weight #Rate charged for packages weighing more than 10lbs.

if package_weight <= 2.0:
    print('The shipping charge will be $', format(rate0to2lbs, '.2f'));
elif package_weight > 2.0 and package_weight <= 6.0:
    print('The shipping charge will be $', format(rate2to6lbs, '.2f'));
elif package_weight > 6.0 and package_weight <= 10.0:
    print('The shipping charge will be $', format(rate6to10lbs, '.2f'));
elif package_weight > 10.0:
    print('The shipping charge will be $', format(rate10lbsplus, '.2f'));
else:
    print ('Invalid weight.')