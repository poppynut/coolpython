class EvenGenerator(object):
    def __init__(self, start_value, end_value):
        self.__start_value = start_value
        self.end_value = end_value

    def generate_value(self):
        while self.__start_value <= self.end_value:
            print self.__start_value,
            self.__start_value += 2


e1 = EvenGenerator(44, 66)
#e1.generate_value()
#print e1.__start_value
#print e1.end_value
#print
e2 = EvenGenerator(100, 112)
e2.generate_value()