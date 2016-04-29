
def center(string_content, width, fill):
    times = (width - len(string_content)) / 2

    fillers = fill * times

    return fillers + string_content + fillers

print center('perl', 8, '-')