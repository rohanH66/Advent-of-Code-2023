times, distances, total = [53, 71, 78, 80],  [275, 1181, 1215, 1524], 1
for a in range(4):
    win_ways = 0
    for b in range(times[a]):
        if (times[a] - b) * b > distances[a]:
            win_ways += 1
    total *= win_ways
print(total)