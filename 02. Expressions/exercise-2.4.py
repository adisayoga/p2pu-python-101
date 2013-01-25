# Exercise 2.4
#
# Assume that we execute the following assignment statements:
#
# width = 17
# height = 12.0
#
# For each of the following expressions, write the value of the expression and
# the type (of the value of the expression).
#
#   1. width / 2
#   2. width / 2.0
#   3. height / 3
#   4. 1 + 2 * 5
#
# Use Python interpreter to check your answers.
#

width = 17
height = 12.0

print type(width / 2)    # <type 'int'>
print type(width / 2.0)  # <type 'float'>
print type(height / 3)   # <type 'float'>
print type(1 + 2 * 5)    # <type 'int'>
