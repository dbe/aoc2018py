from collections import defaultdict
import re

def run(lines):
    #Just get all discreet sections of .'s and #'s
    #The first one is the initial state, and all of the rest of the rules
    initial, *pairs = re.findall(r'[.#]+', '\n'.join(lines))

    #Setup defaultdict mapping pot position to value. Anything not specified will be a '.'
    pots = defaultdict(lambda: '.')
    pots.update( {i: v for i, v in enumerate(initial)} )

    #Clever use of extended ranges to zip even and odd indices from the pairs to combine them
    rules = {i: v for i,v in zip(pairs[::2], pairs[1::2])}



    # for i in range(100):
    #     state = evolve(state, rule_map)
    #     print(''.join(state))
    #
    #
    # total = 0
    # for i in range(len(state)):
    #     if(state[i] == '#'):
    #         total += i - padding
    #
    # return total


def evolve(state, rule_map):
    new_state = ['.'] * len(state)

    for i in range(len(state) - 4):
        stuff = ''.join(state[i:i+5])
        new_state[i + 2] = rule_map[stuff]

    return new_state
