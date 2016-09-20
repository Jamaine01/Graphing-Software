from numpy import *
import matplotlib.pyplot as plt
# import re


start = float(raw_input("Enter minimum X axis value >>>"))
end = float(raw_input("Enter maximum X axis value >>>"))

equation = raw_input("for multiplication, use '*' and for exponents, use '**' \n Do Not Use Spaces \n Ex: 2 squared = 2**2 \n y = ").replace('x', 'i')

print equation 

x = linspace(start, end, 200)
print x

y = [eval(equation) for i in x]
print y

coordinates = zip(x, y)
print "\n Coordinates: \n", coordinates

plt.plot(x, y)
plt.grid(True)
plt.show()