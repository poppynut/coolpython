
s = 'perl scripting'

for item in s:
    if item not in 'aeiou ':
        print "{} : {}".format(item, ord(item))
    else:
        print '****'