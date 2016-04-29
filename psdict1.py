from pprint import pprint as pp

info = {
    'hostname': 'ws1',
    'domain': 'rootcap.in',
    'application': 'apache2',
    'version': 2.2
}

item_key = 'application'

if item_key in info:
    info[item_key] = 'nginx'

info['platform'] = 'linux2'  #add an new element

value = info.pop('domain')

print value
print
pp(info)
