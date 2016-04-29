import re

s = 'the python and the perl scripting'

m = re.search('p.*?n', s, re.I)

if m:
    print "got a match :)"
    print "matched: {}".format(m.group())
    print m.start()
    print m.end()
    print m.span()
    content = s[m.end():]
    content2 = s[:m.start()]

    print "before : |{}|".format(content2)
    print "after : |{}|".format(content)
else:
    print "failed to match :("