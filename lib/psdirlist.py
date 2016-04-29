from pprint import pprint as pp
from os import listdir, stat
from os.path import isfile, join
from time import ctime
from json import dump


class DirListing(object):
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.container = {}
        self.read_directory()

    def read_directory(self):
        for file_item in listdir(self.dir_name):
            abs_path = join(self.dir_name, file_item)

            if isfile(abs_path):
                fs = stat(abs_path)
                value = [fs.st_size, ctime(fs.st_mtime)]

                self.container[file_item] = value


class DirListing2JSON(DirListing):
    def __init__(self, dir_name):
        super(DirListing2JSON, self).__init__(dir_name)

    def to_json(self, json_file):
        fp = open(json_file, 'w')
        dump(self.container, fp, indent=4)
        fp.close()

author = 'jaya'


def sqr_n_cube(value):
    return value ** 2, value ** 3


