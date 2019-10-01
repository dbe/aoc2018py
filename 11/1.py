def run(lines):
    serial = int(lines[0])

    return "Oreo"



def power(x, y, serial):
    return x

def test_power():
    assert(power(3,5,8) == 4)
    assert(power(122,79,57) == -5)
    assert(power(217,196,39) == 0)
    assert(power(101,153,71) == 4)


def test_run():
    assert(run(['18']) == (33, 45))
    assert(run(['42']) == (21, 61))
