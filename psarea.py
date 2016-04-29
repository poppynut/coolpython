from math import pi

radius = float(raw_input('Enter the radius :'))

area = pi * (radius ** 2)

"""
string formatting , returns you the formatted string
"""
content = "radius : %s\narea : %.3f" % (radius, area)
print content.upper()