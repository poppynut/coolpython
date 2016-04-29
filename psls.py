import os
from time import ctime

def ls(path='.'):
    for item in os.listdir(path):
        file_stat = os.stat(item)
        size = file_stat.st_size
        mtime = file_stat.st_mtime

        print "{:>12}  {:>32} {}".format(size, ctime(mtime), item)


ls()
