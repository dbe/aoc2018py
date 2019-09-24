import re

REGEX = r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.'

def run(lines):
    # lines = [
    #     'Step C must be finished before step A can begin.',
    #     'Step C must be finished before step F can begin.',
    #     'Step A must be finished before step B can begin.',
    #     'Step A must be finished before step D can begin.',
    #     'Step B must be finished before step E can begin.',
    #     'Step D must be finished before step E can begin.',
    #     'Step F must be finished before step E can begin.'
    # ]

    instructions = [parse(line) for line in lines]
    step_prereqs = create_step_prereqs(instructions)

    step_list = []

    while(len(step_prereqs) > 0):
        step_list.append(take_step(step_prereqs))

    return ''.join(step_list)

def take_step(prereqs):
    valid_steps = [k for k in prereqs.keys() if prereqs[k] == set()]
    taken = sorted(valid_steps)[0]

    del prereqs[taken]
    for step in prereqs:
        if(taken in prereqs[step]):
            prereqs[step].remove(taken)

    return taken



#Map from step to a set of all prereq steps
#{'C': set(), 'A': {'C'}, 'F': {'C'}, 'B': {'A'}, 'D': {'A'}, 'E': {'F', 'B', 'D'}}
def create_step_prereqs(instructions):
    step_prereqs = {}
    for instruction in instructions:
        if(instruction[0] not in step_prereqs):
            step_prereqs[instruction[0]] = set()

        if(instruction[1] not in step_prereqs):
            step_prereqs[instruction[1]] = set()

        step_prereqs[instruction[1]].add(instruction[0])

    return step_prereqs



#('W', 'G') means that step W has to be done before step G
def parse(line):
    return re.findall(REGEX, line)[0]
