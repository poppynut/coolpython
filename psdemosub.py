import re

s = "setroubleshoot:x:981:978::/var/lib/setroubleshoot:/sbin/nologin"

#s2 = re.sub(':', ',', s)

s2 = re.sub('[AEIOU]', '*', s, flags=re.I)

print s2