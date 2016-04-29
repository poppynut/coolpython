class Car(object):
    engine_state = 'off'



    def start(self):
        if self.engine_state == 'off':
            self.engine_state = 'on'
            print "{} started".format(self)
        else:
            print "{}: already started".format(self)

    def stop(self):
        print "{} stopped".format(self)


c1 = Car()
print c1
print c1.engine_state
c1.start()
c1.start()
print c1.engine_state





