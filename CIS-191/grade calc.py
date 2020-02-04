#---------------
# Author: Kaffeein Bellamy
#
#--------------
>>> def main():
    # Begin count at zero.
    num1 = 0.0
    num2 = 0.0
    num3 = 0.0
    num4 = 0.0
    num5 = 0.0

    num1 = determine_grade()
    num2 = determine_grade()
    num3 = determine_grade()
    num4 = determine_grade()
    num5 = determine_grade()

    # Run the calc_average and determine_grade functions
    average = calc_average(num1, num2, num3, num4, num5)
    if average < 60:
        print('The average score is', average, 'F')
    elif average < 70:
        print('The average score is', average, 'D')
    elif average < 80:
        print('The average score is', average, 'C')
    elif average < 90:
        print('The average score is', average, 'B')
    else:
        print('The average score is', average, 'A')
    

def calc_average(num1, num2, num3, num4, num5):
    average_score = (num1 + num2 + num3 + num4 + num5) / 5
    return average_score

def determine_grade():
    score = int(input('Enter your test score: '))
    if score < 60:
        print("F")
    elif score < 70:
        print("D")
    elif score < 80:
        print("C")
    elif score < 90:
        print("B")
    else:
        print("A")
    return score
    
# Call the main function
main()
