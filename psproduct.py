def product_table(n):
    i = 1
    print '*',

    while i <= n:
        print "{:>3}".format(i),
        i += 1

    i = 1
    print

    while i <= n:
        print i,
        j = 1

        while j <= n:
            print "{:>3}".format(i * j),
            j += 1

        print
        i += 1

number = int(raw_input('Enter your choice :'))
product_table(number)
