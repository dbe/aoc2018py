from collections import deque

def run(lines):
    elements = map(int, lines[0].split(' '))
    # elements = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    tree = deque(elements)

    return parse_node(tree.popleft(), tree.popleft(), tree)

def parse_node(children, metadata, tree):
    total = 0

    for i in range(children):
        total += parse_node(tree.popleft(), tree.popleft(), tree)

    for j in range(metadata):
        total += tree.popleft()

    return total
