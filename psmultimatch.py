import re

s = 'the python and the perl scripting'

for m in re.finditer('p.*?n', s, re.I):
    print m.group()
    print m.span()




