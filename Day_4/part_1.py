import sys
sys.stdin = open("day_4.txt", "r")
cards = list()
total_score = 0
winning_nums = list()
win_new_list = list()
for a in range(203):
    line = input().split()
    new_list = list()
    win_new_list = list()
    for b in range(len(line)):
        try:
            temp = int(line[b])
        except:
            continue
        if b > 1 and b < 12:
            win_new_list.append(temp)
        else:
            new_list.append(temp)
    cards.append(new_list)
    winning_nums.append(win_new_list)
    print(cards[a], "\n", win_new_list)
count = 0    
for c in cards:
    score = 0
    
    curr_wins = winning_nums[count]
    print(curr_wins, c)
    for card in c:
        
        if card in curr_wins:
            if score == 0:
                score += 1
                print(score, card)
            else:
                score *= 2
                
                print(score, card)
        else:
            # print(card, "PASS", score)
            pass
    total_score += score  
    count += 1      
   
    
print(total_score)

    