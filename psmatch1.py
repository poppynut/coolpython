import re

s = 'the python and the perl scripting'

m = re.match('python', s, re.I)

if m:
    print "got a match :)"
else:
    print "failed to match :("