from collections import deque

def run(lines):
    elements = map(int, lines[0].split(' '))
    # elements = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    tree = deque(elements)

    return value_node(tree.popleft(), tree.popleft(), tree)

def value_node(num_children, meta, tree):
    if(num_children == 0):
        return sum([tree.popleft() for i in range(meta)])

    children = []
    value = 0

    for i in range(num_children):
        children.append( value_node(tree.popleft(), tree.popleft(), tree) )

    for j in range(meta):
        index = tree.popleft()
        if(index > 0 and index <= len(children)):
            value += children[index - 1]

    return value
