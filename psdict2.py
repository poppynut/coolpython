from pprint import pprint as pp

info = {
    'hostname': 'ws1',
    'domain': 'rootcap.in',
    'application': 'apache2',
    'version': 2.2
}
"""
print info.get('hostname')
print info.get('domain')
print info.get('version')
"""

print info.keys()
print
print info.values()
print
print info.items()