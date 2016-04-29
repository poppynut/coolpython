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


class Employee(Person):
    def __init__(self, eid, first_name, last_name, age, gender, dept, desg):
        self.eid = eid
        self.dept = dept
        self.desg = desg
        super(Employee, self).__init__(first_name, last_name, age, gender)

    def get_info(self):
        print "id :", self.eid
        super(Employee, self).get_info()
        print "dept :", self.dept
        print "desg :", self.desg


e = Employee('v4001', 'guido', 'rossum', 4, 'male', 'sales', 'clerk')
e.get_info()