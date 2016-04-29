"""
items = 1, 3.3, 'peter pan', 'R'
print items
"""
#tuple assignment or parallel assignment

name, age, gender = 'sara', 4, 'female'

print name
print gender

#functions could return more than one value
q, r = divmod(5, 2)
print q
print r


def sqr_and_cube(n):
    return n**2, n**3

print sqr_and_cube(6)