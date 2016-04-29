class EvenGenerator(object):
    def __init__(self, start_value, end_value):
        self.start_value = start_value
        self.end_value = end_value

    def generate_value(self):
        while self.start_value <= self.end_value:
            print self.start_value,
            self.start_value += 2


e1 = EvenGenerator(44, 66)
#e1.generate_value()
print e1.start_value
print e1.end_value
print
e2 = EvenGenerator(100, 112)
e2.generate_value()