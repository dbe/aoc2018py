import re

REGEX = r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)'

def run(lines):
    parsed_lines = [parse(line) for line in lines]
    events = [normalize_dates(line) for line in parsed_lines]
    grouped = group_by_date(events)

    for date in grouped:
        print(date)
        print(grouped[date]['guard'])

def parse(line):
    return re.findall(REGEX, line)[0]

#Input: (min, date, action)
# Output: {'3-11':
#             {guard: 255,
#              actions: [
#                 (22, 'up'),
#                 (33, 'down')
#              ]}
#         }

def parse_guard(action):
    regex = r'Guard #(\d+) begins shift'
    return int(re.findall(regex, action)[0])

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
