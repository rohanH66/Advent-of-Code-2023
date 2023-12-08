def check_type(letters):
    five_of_a_kind = False
    four_of_a_kind = False
    full_house = False
    three_of_a_kind = False
    two_pair = False
    one_pair = False
    high_card = False
    
    one = letters.count(letters[0])
    two = letters.count(letters[1])
    three = letters.count(letters[2])
    four = letters.count(letters[3])
    five = letters.count(letters[4])
    
    if one == 5 or two == 5 or three == 5 or four == 5 or five == 5:
        five_of_a_kind = True
        print(letters)
    elif one == 4 or two == 4 or three == 4 or four == 4 or five == 4:
        four_of_a_kind = True
        print(letters)
    elif one == 3 or two == 3 or three == 3 or four == 3 or five == 3:
        if one == 2 or two == 2 or three == 2 or four == 2 or five == 2:
            full_house = True
        else:
            three_of_a_kind = True
    
    
            
import sys
sys.stdin = open("input.txt", "r")
overall = dict()
for i in range(20):
    card, bet = input().split()
    overall[card] = int(bet)
    
for i in overall:
    temp = list()
    for j in i:
        temp.append(j)
    check_type(temp)
        

print(overall)




    
    
    