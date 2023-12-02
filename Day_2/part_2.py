import sys
sys.stdin = open("day_2.txt", "r")

count = 0
for i in range(100):
    sentence = input().split()
    game = int(sentence[1].replace(":", ""))
    curr_max_red, curr_max_blue, curr_max_green = 0, 0, 0
    
    for a in range(len(sentence)):
        try:
            curr = sentence[a + 2]
            next_curr = sentence[a+3].replace(",", "").replace(";", "").replace(":", "")
        except:
            pass
        try:
            curr = int(curr)
            if next_curr == "red":
                if curr > curr_max_red:
                    curr_max_red = curr
            elif next_curr == "green":
                if curr > curr_max_green:
                    curr_max_green = curr
            elif next_curr == "blue":
                if curr > curr_max_blue:
                    curr_max_blue = curr
        except:
            pass
    count += curr_max_red * curr_max_blue * curr_max_green

print(count)