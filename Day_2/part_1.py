import sys
sys.stdin = open("day_2.txt", "r")

count = 0
fail = bool()
for i in range(100):
    sentence = input().split()
    game = int(sentence[1].replace(":", ""))
    for a in range(len(sentence)):
        try:
            curr = sentence[a + 2]
            next_curr = sentence[a+3].replace(",", "").replace(";", "").replace(":", "")
        except:
            pass
        try:
            curr = int(curr)
            if next_curr == "red" and curr > 12:
                fail = True
            elif next_curr == "green" and curr > 13:
                fail = True
            elif next_curr == "blue" and curr > 14:
                fail = True   
        except:
            pass
    if fail == False:
        count += game
    fail = False

print(count)      