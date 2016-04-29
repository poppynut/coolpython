import MySQLdb
from csv import reader


class CSV2DB(object):
    def __connect_db(self):
        return MySQLdb.connect('localhost', 'root', '', 'apr27')

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.connection = self.__connect_db()
        self.data_set = []
        self.__parse_csv()
        self.__do_insert()

    def __parse_csv(self):
        for record in reader(open(self.csv_file), delimiter=':'):
            self.data_set.append(record)

    def __do_insert(self):
        cur = self.connection.cursor()
        query = 'insert into passwd values (%s, %s, %s, %s, %s, %s, %s)'
        cur.executemany(query, self.data_set)
        self.connection.commit()
        cur.close()

    def __del__(self):
        self.connection.close()

CSV2DB('/etc/passwd')


