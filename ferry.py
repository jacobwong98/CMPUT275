events = dict()

time = 0
location = 'W'

for w in input().split():
    events.update({int(w):'W'})
for e in input().split():
    events.update({int(e):'E'})

for event in sorted(events):
    if event > time:
        time = events

    if events[event] != location:
        time += 100
    else:
        if location == 'W':
            location = 'E'
        else:
            location = 'W'
    time += 100

print(time)
