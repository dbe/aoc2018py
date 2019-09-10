def run(lines):
    g = gen(list(map(int, lines)))

    s = {0}
    current = 0

    while(True):
        current += next(g)
        if current in s:
            return current
        else:
            s.add(current)


def gen(lst):
    l = len(lst)
    i = 0

    while(True):
        yield(lst[i % l])
        i += 1
