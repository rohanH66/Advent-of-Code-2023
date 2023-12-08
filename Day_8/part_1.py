import sys
sys.stdin = open("in.txt", "r")
instructions, tuples, steps = input(), list(), 0

for i in range(790):
    overall = input().replace(" =", "").replace("(", "").replace(",", "").replace(")", "").split()
    tuples.append((overall[0], overall[1], overall[2]))
 
for b in tuples: 
    if b[0] == "AAA": curr_tuple = b

while True:
    for a in instructions:
        if a == "L": new = curr_tuple[1]
        else: new = curr_tuple[2]
        
        steps += 1    
        if new == "ZZZ": break
        
        for b in tuples:
            if b[0] == new: curr_tuple = b
    if new == "ZZZ": break
       
print(steps)