#-------------------------------------------------------------------------------
# Name:        Days of the Week
# Purpose:     Homework
#
# Author:      Kaffeein Bellamy
#
# Created:     11/09/2018
#-------------------------------------------------------------------------------

#Get the number for the day of the week.

dayOfWeek = int(input("Enter the number for the day of the week (1-7)"));

#Determines which day to display

if dayOfWeek == 1:
    print("Monday");
elif dayOfWeek == 2:
    print("Tuesday");
elif dayOfWeek == 3:
    print("Wednesday");
elif dayOfWeek == 4:
    print("Thursday");
elif dayOfWeek == 5:
    print("Friday");
elif dayOfWeek == 6:
    print("Saturday");
elif dayOfWeek == 7:
    print ("Sunday")
else:
    print("Please enter a valid number");