def run(input):
    foo = list(map(int, input.strip().split('\n')))
    g = gen(foo)

    s = {0}
    current = 0

    while(True):
        current += next(g)
        if current in s:
            print(current)
            return
        else:
            s.add(current)


def gen(lst):
    l = len(lst)
    i = 0

    while(True):
        yield(lst[i % l])
        i += 1
