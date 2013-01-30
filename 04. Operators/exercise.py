# Create simple Python script program to perform numeric calculations and 
# output results

# Volume of a Cylinder
# V = pi * r * r * h

pi = 3.14159265
r = float(raw_input('Radius: '))
h = float(raw_input('Height: '))

v = pi * r * r * h
print 'Volume: ' + str(v)