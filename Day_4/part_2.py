import sys
sys.stdin = open("day_4.txt", "r")
cards = list()
total_score = 0
winning_nums = list()
win_new_list = list()
for a in range(6):
    line = input().split()
    new_list = list()
    win_new_list = list()
    for b in range(len(line)):
        try:
            temp = int(line[b])
        except:
            continue
        if b > 1 and b < 7:
            win_new_list.append(temp)
        else:
            new_list.append(temp)
    cards.append(new_list)
    winning_nums.append(win_new_list)
    # print(cards[a], "\n", win_new_list)
count = 0 
overall_counter = 0 
matches = 0  

copies = [0 for a in range(len(cards))]
print(copies)
for c in cards:
    score = 0
    
    curr_wins = winning_nums[count]
    # print(curr_wins, c)
    for f in range(len(c)):
        card = c[f]
        if card in curr_wins:
            matches += 1
        else:
            # print(card, "PASS", score)
            pass
    for d in range(matches):
        try:
            copies[card + d] += 1
        except:
            pass
        
    count += 1  
count = 0
for m in range(len(cards)):
    score = 0
    c = cards[m]
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
    total_score += (score * copies[m])  
    count += 1      
   
    

  
total_score += score  
print(copies)
        
   
    
print(total_score)

    