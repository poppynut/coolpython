i = 1
#pydev
while i <= 10:
    if i == 1:
        print 'one'
    elif i == 2:
        print 'ii'
    elif i == 5:
        i += 1
        continue
    elif i == 7:
        break
    else:
        print i
    i += 1

print '----'