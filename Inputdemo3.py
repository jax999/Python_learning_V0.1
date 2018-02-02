#Ask for age and how far you want to calculate
"""Stuff""" #Docline

# Syntax for age and age ahead
print('What is your age?\n\n')
MYAGE = input('Input age\n')
MYAGE = int(MYAGE)
# syntax for calculation
YEARS = input('Input how many years ahead you want it to calculate\n')
YEARS = int(YEARS)

if  MYAGE < 40:
    print("Still Youngster")
else:
# Prints sum of syntax 7 och 10
    print('\n')
    print('You will be', MYAGE + YEARS, 'years old','and matured')
    print('\n')
