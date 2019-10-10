def run(lines):
    initial = int(lines[0])
    board = [3, 7]
    #Index into board for each elfs current recipe
    elves = [0, 1]

    return last_ten(board, elves, initial)


def last_ten(board, elves, initial):
    while(len(board) < initial + 10):
        tick(board, elves)

    return ''.join(map(str, board[initial:initial + 10]))

#Mutates both board and elves
def tick(board, elves):
    append_scores(board, elves)
    update_elves(board, elves)

#Mutates elves
def update_elves(board, elves):
    for i, elf in enumerate(elves):
        elves[i] = (elf + (board[elf] + 1)) % len(board)

#Mutates board
def append_scores(board, elves):
    new = sum( [board[elf] for elf in elves ] )
    board.extend(map(int, list(str(new))))

######################TESTS##########################

#####################################################
def test_append_scores():
    board = [3, 7]
    elves = [0, 1]

    append_scores(board, elves)
    assert(board == [3, 7, 1, 0])

    board = [3,7,1,0,1,0,1,2,4,5,1]
    elves = [8, 4]

    append_scores(board, elves)
    assert(board == [3,7,1,0,1,0,1,2,4,5,1,5])

def test_tick():
    board = [3, 7]
    elves = [0, 1]

    expected = [
        {'board': [3,7,1,0], 'elves': [0,1] },
        {'board': [3,7,1,0,1,0], 'elves': [4,3] },
        {'board': [3,7,1,0,1,0,1], 'elves': [6,4] },
        {'board': [3,7,1,0,1,0,1,2], 'elves': [0,6] },
        {'board': [3,7,1,0,1,0,1,2,4], 'elves': [4,8] },
        {'board': [3,7,1,0,1,0,1,2,4,5], 'elves': [6,3] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1], 'elves': [8,4] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1,5], 'elves': [1,6] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1,5,8], 'elves': [9,8] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1,5,8,9], 'elves': [1,13] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1,5,8,9,1,6], 'elves': [9,7] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1,5,8,9,1,6,7], 'elves': [15,10] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1,5,8,9,1,6,7,7], 'elves': [4,12] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1,5,8,9,1,6,7,7,9], 'elves': [6,2] },
        {'board': [3,7,1,0,1,0,1,2,4,5,1,5,8,9,1,6,7,7,9,2], 'elves': [8,4] },

    ]

    for i in range(len(expected)):
        tick(board, elves)
        assert(board == expected[i]['board'])
        assert(elves == expected[i]['elves'])


def test_last_ten():
    expected = [
        '0124515891',
        '9251071085',
        '5941429882',
    ]

    for i, initial in enumerate([5, 18, 2018]):
        board = [3, 7]
        elves = [0, 1]
        assert( last_ten(board, elves, initial) == expected[i] )
