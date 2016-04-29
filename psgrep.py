import re
import fileinput


def grep_me(file_name, pattern):
    for line in fileinput.input([file_name]):
        if re.search(pattern, line, re.I):
            print line,


#grep_me('/etc/passwd', 'bash')
#grep_me('/etc/passwd', '([5-9]\d\d)|([1-9]\d\d\d+)')

grep_me('decimals', r'(\d)(\d)\.\2\1')