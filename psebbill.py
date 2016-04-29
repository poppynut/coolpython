def compute(units):
    amount = 0
    if units < 0:
        error_mesg = "value to the units should be +ve : {}".format(units)
        raise ValueError(error_mesg)
    elif units <= 100:
        amount = units
    elif units <= 200:
        amount = units * 1.5
    elif units <= 500:
        amount = (200 * 2) + (units - 200) * 3
    elif units > 500:
        amount = (200 * 3) + (300 * 4) + (units - 500) * 5.75

    return amount

try:
    consumed_units = int(raw_input('Enter the consumed units :'))
    billable = compute(consumed_units)

    print "billable : {:.2f}".format(billable)
except ValueError, e:
    print e