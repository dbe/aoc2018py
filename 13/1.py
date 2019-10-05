import pytest

def run(lines):
    cave = parse_lines(lines)

    for y, line in enumerate(lines):
        for x, col in enumerate(line):
            print(f"{x},{y}")

def find_carts(cave):
    carts = []

    for y, line in enumerate(cave):
        for x, tile in enumerate(line):
            if(is_cart(tile)):
                carts.append((x, y))

    return carts

def is_cart(tile):
    return (
        tile == '>' or
        tile == '<' or
        tile == 'v' or
        tile == '^'
    )

def parse_lines(lines):
    print(f"lines: {type(lines)}")
    return [list(line) for line in lines]

### TESTS ###
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
### TESTS ###

@pytest.fixture
def cave():
    with open('13/in.txt') as f:
        return parse_lines(f.read().strip().split('\n'))

def test_find_carts(cave):
    carts = find_carts(cave)

    assert(len(carts) == 2)
    assert(carts[0] == (2, 0))
    assert(carts[1] == (9, 3))

def test_is_cart():
    assert( is_cart("<-") == False )
    assert( is_cart("-") == False )
    assert( is_cart("+") == False )
    assert( is_cart("\\") == False )
    assert( is_cart("/") == False )
    assert( is_cart("|") == False )

    assert( is_cart(">") == True )
    assert( is_cart("<") == True )
    assert( is_cart("v") == True )
    assert( is_cart("^") == True )
