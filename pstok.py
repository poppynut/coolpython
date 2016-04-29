s = 'root:x:0:0:root:/root:/bin/bash'

items = s.split(':')

print items

print s.split(':')[0]


delimiter = ','
s2 = delimiter.join(items)
print s2