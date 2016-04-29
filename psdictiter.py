from pprint import pprint as pp

info = {
    'hostname': 'ws1',
    'domain': 'rootcap.in',
    'application': 'apache2',
    'version': 2.2
}

for key in info:
    print "{} -> {}".format(key, info.get(key))