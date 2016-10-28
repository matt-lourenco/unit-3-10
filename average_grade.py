# Created on 28 oct 2016
# Created by: Matthew Lourenco
# this is a program that constantly displayes the average until -1 is entered
grade_table = []
print('Enter a number from 0-100. Enter -1 to end.')
while True:
    try:
        grade = raw_input()
        grade = float(grade)
        if grade >= 0:
            if grade <= 100:
                average = float(0)
                grade_table.append(grade)
                for index in range(0, len(grade_table)):
                    average = average + grade_table[index]
                average = average / len(grade_table)
                print('The numbers are: ' + str(grade_table) + '\nThe average is: ' + str(average))
            else:
                print('Please enter a number from 0-100. Enter -1 to end.')
        else:
            print('Ended')
            break
    except:
        print('Please enter a real number.')
