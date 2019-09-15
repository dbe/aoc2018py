def run(lines):
    #Setup
    poly = lines[0]
    out = list()

    #Stack based algo
    for a in poly:
        if(len(out) == 0):
            out.append(a)
        elif(out[-1] != a and out[-1] == a.swapcase()):
            out.pop()
        else:
            out.append(a)

    return len(out)
