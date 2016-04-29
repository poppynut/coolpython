class UserList(object):
    def __init__(self, data_file):
        self.data_file = data_file
        self.user_list = []
        self.__get_user_list()

    def __get_user_list(self):
        fp = open(self.data_file)

        for line in fp:
            login = line.split(':')[0]
            login = login.title()
            self.user_list.append(login)

        fp.close()

    def put_user_list(self, target_file=None):
        self.user_list.sort()
        line_no = 1

        if target_file:
            fw = open(target_file, 'w')

            for login in self.user_list:
                content = "{:>6}  {}".format(line_no, login)
                print content
                fw.write(content + "\n")
                line_no += 1

            fw.close()
        else:
            for login in self.user_list:
                print "{:>6}  {}".format(line_no, login)
                line_no += 1


ul = UserList('/etc/passwd')
ul.put_user_list('userlist.dat')