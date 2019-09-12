import re

REGEX = r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)'

#This one got a little messy
def run(lines):
    parsed_lines = [parse(line) for line in lines]
    events = [normalize_dates(line) for line in parsed_lines]
    grouped = group_by_date(events)

    #Add sleep schedule to each date
    for date in grouped:
        sleep = sleep_by_min(grouped[date]['actions'])
        grouped[date]['sleep'] = sleep

    schedules = get_sleep_schedules_by_guard(grouped)

    #Figure out which guard slept the most at a given minute
    final_guard = None
    final_min = -1
    final_times_slept = 0

    for guard in schedules:
        schedule = schedules[guard]
        min, times = most_slept_min(schedule)
        if(times > final_times_slept):
            final_times_slept = times
            final_min = min
            final_guard = guard

    return final_guard * final_min


def parse(line):
    return re.findall(REGEX, line)[0]

def parse_guard(action):
    regex = r'Guard #(\d+) begins shift'
    return int(re.findall(regex, action)[0])

def get_sleep_schedules_by_guard(grouped):
    sleep_schedules = {}

    for date in grouped:
        guard = grouped[date]['guard']
        schedules = sleep_schedules.get(guard, [])
        schedules.append(grouped[date]['sleep'])

        sleep_schedules[guard] = schedules

    return sleep_schedules

#Return which minute was slept the most, and how many times
def most_slept_min(sleep_schedule):
    sums = list(map(sum, zip(*sleep_schedule)))
    times = max(sums)

    return (sums.index(times), times)

def sleepiest_guard(grouped):
    by_guard = sleep_count_by_guard(grouped)

    most_sleep = -1
    sleepy_guy = None

    for guard in by_guard:
        if(by_guard[guard] > most_sleep):
            most_sleep = by_guard[guard]
            sleepy_guy = guard

    return sleepy_guy


def sleep_count_by_guard(grouped):
    by_guard = {}

    for date in grouped:
        guard = grouped[date]['guard']
        sleep = by_guard.get(guard, 0)
        sleep += sum(grouped[date]['sleep'])
        by_guard[guard] = sleep

    return by_guard

def sleep_by_min(actions):
    sleep = [0] * 60
    sorted_actions = sorted(actions, key=lambda action: action[0])

    #Take every 2 actions (paired up/down)
    for i in range(0, int(len(sorted_actions) / 2)):
        up = sorted_actions[i * 2][0]
        down = sorted_actions[i * 2 + 1][0]

        for j in range(up, down):
            sleep[j] = 1

    return sleep


#Input: (min, date, action)
# Output: {'3-11':
#             {guard: 255,
#              actions: [
#                 (22, 'up'),
#                 (33, 'down')
#              ]}
#         }
def group_by_date(events):
    by_date = {}

    for event in events:
        min, date, action = event

        spec = by_date.get(date, {'actions':[]})

        if(action == 'wakes up'):
            spec['actions'].append((min, 'up'))
        elif(action == 'falls asleep'):
            spec['actions'].append((min, 'down'))
        else:
            spec['guard'] = parse_guard(action)

        by_date[date] = spec


    return by_date


#{min, date, action} // {22, '3-11', 'wakes up'}
def normalize_dates(parsed):
    (_, month, day, hour, min, action) = parsed
    month, day, hour, min = int(month), int(day), int(hour), int(min)

    #Guard starts event, need to normalize to next day
    if(hour == 23):
        #Feb
        if(month == 2 and day == 28):
            day = 1
            month = 3
        #30 days hath Sept, April, June and November
        elif(day == 30 and (month == 4 or month == 6 or month == 9 or month == 11)):
            day = 1
            month += 1
        #All 31 day months
        elif(day == 31):
            day = 1

            #Handle December looping to Jan
            if(month == 12):
                month = 1
            else:
                month += 1
        else:
            day += 1

    return (min, f"{month}-{day}", action)
