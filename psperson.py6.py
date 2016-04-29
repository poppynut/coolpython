class Person(object):
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def get_info(self):
        print "first name :", self.first_name
        print "last name :", self.last_name
        print "age :", self.age
        print "gender :", self.gender

p = Person('larry', 'wall', 4, 'male')
p.get_info()