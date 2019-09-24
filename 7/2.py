from string import ascii_uppercase
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
    spr = create_step_prereqs(instructions)
    workers = [{'step': None, 'time_left': 0} for _ in range(5)]
    steps_taken = []

    total_time = 0
    while(len(spr) > 0):
        #Assign eligible workers
        for worker in workers:
            #Worker is free and there is an available step to take
            if(worker['step'] == None and set() in spr.values()):
                worker['step'], worker['time_left'] = take_job(spr)

        #Resolve the next to finish job
        finished, time = resolve_workers(workers)
        total_time += time

        resolve_spr(finished, spr)
        steps_taken.append(finished)

    # return ''.join(steps_taken)
    return total_time

def resolve_spr(finished, spr):
    for step in spr:
        if(finished in spr[step]):
            spr[step].remove(finished)

def resolve_workers(workers):
    busy_workers = list(filter(lambda worker: worker['step'] != None, workers))

    ntf = sorted(busy_workers, key=lambda worker: worker['time_left'])[0]
    finished, time = ntf['step'], ntf['time_left']

    #Progress time by reducing time_left for each busy worker
    for worker in busy_workers:
        worker['time_left'] -= time

    #Let worker who is next to finish actually finish his job
    ntf['step'] = None

    return finished, time


def take_job(spr):
    step = sorted([k for k in spr.keys() if spr[k] == set()])[0]
    del spr[step]

    return (step, ascii_uppercase.index(step) + 61)

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
