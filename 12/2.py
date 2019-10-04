from collections import defaultdict
import re

GENERATIONS = 1000

def run(lines):
    #Just get all discreet sections of .'s and #'s
    #The first one is the initial state, and all of the rest of the rules
    initial, *pairs = re.findall(r'[.#]+', '\n'.join(lines))

    #Setup defaultdict mapping pot position to value. Anything not specified will be a '.'
    pots = defaultdict(lambda: '.')
    pots.update( {i: v for i, v in enumerate(initial)} )

    #Clever use of extended ranges to zip even and odd indices from the pairs to combine them
    rules = {i: v for i,v in zip(pairs[::2], pairs[1::2])}
    seen = set()

    for time in range(GENERATIONS):
        seen.add(trimmed_pattern(pots))
        # pretty_print(pots, time)
        evolve(pots, rules)
        if(trimmed_pattern(pots) in seen):
            # print("FOUND IT")
            break

    # pretty_print(pots, time + 1)

    return score(pots, (50 * 10**9) - (time + 1))

def score(pots, offset=0):
    score = 0
    for i in range(min(pots), max(pots) + 1):
        if(pots[i] == '#'):
            score += i + offset

    return score

def trimmed_pattern(pots):
    return ''.join([pots[i] for i in range(min(pots), max(pots) + 1) ] ).strip('.')

def pretty_print(pots, gen):
    print(gen, end=':')
    print(score(pots), end=": ")
    print(trimmed_pattern(pots))

def evolve(pots, rules):
    new_pots = {}
    #Increases the size of search by 3 pots on each end
    for i in range(min(pots) - 3, max(pots)):
        slice = ''.join([pots[j] for j in range(i, i+5)])
        new_pots[i + 2] = rules.get(slice, '.')

    pots.update(new_pots)
