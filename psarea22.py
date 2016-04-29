from math import pi

radius = float(raw_input('Enter the radius :'))

area = pi * (radius ** 2)

"""
{index:fmt-string}
"""
#print "radius : {0}\narea : {1:.3f}".format(radius, area)
print "radius : {}\narea : {:.3f}".format(radius, area)

