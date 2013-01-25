# Exercise 2.3
#
# Write a program to prompt the user for hours and rate per hour to compute
# gross pay
#
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
#

hours = int(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))

pay = hours * rate
print 'Pay: ' + str(pay)
