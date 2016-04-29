import re
import fileinput


def fix_it(pattern, replacement):
    for line in fileinput.input(inplace=True, backup='.bak'):
        print re.sub(pattern, replacement, line, flags=re.I),

fix_it('(\d+)', r'[\1]')