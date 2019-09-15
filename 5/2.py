from string import ascii_lowercase

def run(lines):
    poly = lines[0]
    shortest = len(poly)

    for c in ascii_lowercase:
        length = shrink(poly, c)

        if length < shortest:
            shortest = length

    return shortest


def shrink(poly, skip):
    out = list()

    #Stack based algo
    for a in poly:
        if(a.lower() == skip):
            pass
        elif(len(out) == 0):
            out.append(a)
        elif(out[-1] != a and out[-1] == a.swapcase()):
            out.pop()
        else:
            out.append(a)

    return len(out)
