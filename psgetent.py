def getent(dbname, search_key):
    data_file = None
    lookup = {}

    if dbname == 'passwd':
        data_file = '/etc/passwd'

    fp = open(data_file)

    for line in fp:
        login = line.split(':')[0]
        lookup[login] = line

    fp.close()

    return lookup.get(search_key)

print getent('passwd', 'root')