import re
import pwd


s = 'root,x;0:0,root,/root'

items = re.split('[,;:]', s)

for item in items:
    print item

