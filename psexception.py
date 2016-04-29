def safe_float(value):
    try:
        return float(value)
    except ValueError, e:
        print e
    except TypeError, e:
        print e
    except StandardError:
        print 'handled by the parent class'


print safe_float(124)
print safe_float([1, 2, 3])
