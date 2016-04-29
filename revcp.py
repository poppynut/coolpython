from sys import argv, stderr


def usage():
    print >>stderr, "Usage :"
    print >>stderr, "{} source-file target-file".format(argv[0])
    exit(1)


def reverse_copy(source, target):
    fp = open(source)
    fw = open(target, 'w')
    content = fp.readlines()
    content.reverse()

    fw.writelines(content)
    fw.close()
    fp.close()

if len(argv) != 3:
    usage()

reverse_copy(argv[1], argv[2])