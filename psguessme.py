from random import randint


class GuessMe(object):
    def __init__(self):
        self.rand_value = randint(1, 1000)
        self.user_value = None
        self.max_chance = 10
        self.do_play()

    """
    def __del__(self):
        print "{} am getting destoryed".format(self)
    """

    def do_play(self):
        chance = 1
        w_flag = 0

        while chance <= self.max_chance:

            try:
                prompt = "Chance: {}\nenter the value:".format(chance)
                self.user_value = int(raw_input(prompt))
            except ValueError, e:
                print
                continue

            if self.user_value == self.rand_value:
                print "you won :) !!!!!!!!!"
                w_flag = 1
                break
            elif self.user_value < self.rand_value:
                print "lesser :", self.user_value
            elif self.user_value > self.rand_value:
                print "greater :", self.user_value

            print
            chance += 1

        if w_flag == 0:
            print "you lost losser :(.........."


GuessMe()
