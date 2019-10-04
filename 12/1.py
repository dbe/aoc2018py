import re

REGEX = r'(.{5}) => (.)'

def run(lines):
#     lines ='''initial state: #..#.#..##......###...###
#
# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #'''.split('\n')

    padding = 50
    state = list(padding * '.' + lines[0][15:] + padding * '.')

    rules = [lines[i] for i in range(2, len(lines))]
    rule_map = {}

    for rule in rules:
        (a, b) = re.findall(REGEX, rule)[0]
        rule_map[a] = b

    print(f"rule_map: {rule_map}")

    print(''.join(state))
    for i in range(100):
        state = evolve(state, rule_map)
        print(''.join(state))


    total = 0
    for i in range(len(state)):
        if(state[i] == '#'):
            total += i - padding

    return total


def evolve(state, rule_map):
    new_state = ['.'] * len(state)

    for i in range(len(state) - 4):
        stuff = ''.join(state[i:i+5])
        new_state[i + 2] = rule_map[stuff]

    return new_state
