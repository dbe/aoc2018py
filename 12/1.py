from collections import defaultdict
import re

GENERATIONS = 20

def run(lines):
    #Just get all discreet sections of .'s and #'s
    #The first one is the initial state, and all of the rest of the rules
    initial, *pairs = re.findall(r'[.#]+', '\n'.join(lines))

    #Setup defaultdict mapping pot position to value. Anything not specified will be a '.'
    pots = defaultdict(lambda: '.')
    pots.update( {i: v for i, v in enumerate(initial)} )

    #Clever use of extended ranges to zip even and odd indices from the pairs to combine them
    rules = {i: v for i,v in zip(pairs[::2], pairs[1::2])}

    pretty_print(pots)
    for time in range(GENERATIONS):
        evolve(pots, rules)
        pretty_print(pots)

    return score(pots)

def score(pots):
    score = 0
    for i in range(min(pots), max(pots) + 1):
        if(pots[i] == '#'):
            score += i

    return score

def pretty_print(pots):
    for i in range(min(pots), max(pots) + 1):
        print(pots[i], end='')
    print()

def evolve(pots, rules):
    new_pots = {}
    #Increases the size of search by 2 pots on each end
    for i in range(min(pots) - 2, max(pots) - 1):
        slice = ''.join([pots[j] for j in range(i, i+5)])
        new_pots[i + 2] = rules.get(slice, '.')

    pots.update(new_pots)
