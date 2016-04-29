fp = open(r'/etc/passwd')

for line in fp:
    print line,

fp.close()