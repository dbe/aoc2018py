def run(lines):
    pattern = lines[0]
    board = '37'
    #Index into board for each elfs current recipe
    elves = [0, 1]

    return first_pattern(board, elves, pattern)

def first_pattern(board, elves, pattern):
    r = (len(pattern) + 1) * -1

    i = 0
    while(True):
        if(i % 1000000 == 0):
            print(i)

        board, elves = tick(board, elves)

        if(pattern in board[r:]):
            return board.index(pattern)

        i += 1

        # if(pattern == ''.join(map(str, board[-7:-1]))):
        #     return len(board) - 7
        # elif(pattern == ''.join(map(str, board[-6:]))):
        #     return len(board) - 6

def last_ten(board, elves, initial):
    while(len(board) < initial + 10):
        board, elves = tick(board, elves)

    return ''.join(map(str, board[initial:initial + 10]))

def tick(board, elves):
    board = append_scores(board, elves)
    update_elves(board, elves)
    return (board, elves)

#Mutates elves
def update_elves(board, elves):
    for i, elf in enumerate(elves):
        elves[i] = (elf + (int(board[elf]) + 1)) % len(board)

    return elves

#Mutates board
def append_scores(board, elves):
    new = sum( [int(board[elf]) for elf in elves ] )
    return board + str(new)

######################TESTS##########################

#####################################################
def test_append_scores():
    board = '37'
    elves = [0, 1]

    assert(append_scores(board, elves) == '3710')

    board = '37101012451'
    elves = [8, 4]

    assert(append_scores(board, elves) == '371010124515')

def test_tick():
    board = '37'
    elves = [0, 1]

    expected = [
        {'board': '3710', 'elves': [0,1] },
        {'board': '371010', 'elves': [4,3] },
        {'board': '3710101', 'elves': [6,4] },
        {'board': '37101012', 'elves': [0,6] },
        {'board': '371010124', 'elves': [4,8] },
        {'board': '3710101245', 'elves': [6,3] },
        {'board': '37101012451', 'elves': [8,4] },
        {'board': '371010124515', 'elves': [1,6] },
        {'board': '3710101245158', 'elves': [9,8] },
        {'board': '37101012451589', 'elves': [1,13] },
        {'board': '3710101245158916', 'elves': [9,7] },
        {'board': '37101012451589167', 'elves': [15,10] },
        {'board': '371010124515891677', 'elves': [4,12] },
        {'board': '3710101245158916779', 'elves': [6,2] },
        {'board': '37101012451589167792', 'elves': [8,4] },

    ]

    for i in range(len(expected)):
        (board, elves) = tick(board, elves)
        assert(board == expected[i]['board'])
        assert(elves == expected[i]['elves'])


def test_last_ten():
    expected = [
        '0124515891',
        '9251071085',
        '5941429882',
    ]

    for i, initial in enumerate([5, 18, 2018]):
        board = '37'
        elves = [0, 1]
        assert( last_ten(board, elves, initial) == expected[i] )

def test_first_pattern():
    expected = [
        9,
        5,
        18,
        2018,
        10
    ]

    for i, pattern in enumerate(['51589', '01245', '92510', '59414', '15891']):
        board = '37'
        elves = [0, 1]
        assert( first_pattern(board, elves, pattern) == expected[i] )
