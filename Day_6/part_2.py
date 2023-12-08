times, distances, total = [53717880],  [275118112151524], 1
for a in range(1):
    win_ways = 0
    for b in range(times[a]):
        if (times[a] - b) * b > distances[a]:
            win_ways += 1
    total *= win_ways
print(total)

