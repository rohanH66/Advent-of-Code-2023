import sys
sys.stdin = open("day_3.txt", "r")
words = [input() for x in range(140)]
count = 0
overall_count = 0
special_chacters = "*"
special_next = bool()
special_above = bool()
total = 0
for i in range(len(words)):
    
    try:
        before = words[i-1]
    except:
        before = "." * 140
    
    try:
        new = words[i+1]
    except:
        new = "." * 140
    
    curr = words[i]
    
    mod = 0
    
    mod = 0
    for c in range(len(curr)):
        
        
        if c + mod > len(curr) - 1:
            
            break
        else:
            letter = c + mod
            # print("letter", letter, c, mod)
        # print(letter)
        print(curr[letter], letter, "letter", f"c == {c}", f"mod == {mod}")
        digits = 0
        # print(curr[letter], letter, "letter")
        
        
        
        
        if (curr[letter] == "." or curr[letter] in special_chacters):
            continue
        
        if (curr[letter]).isdigit():
            
            if (curr[letter + 1]).isdigit() and (curr[letter + 2]).isdigit():
                digits = 3
                # print(int(curr[letter] + curr[letter + 1] + curr[letter + 2]))
                # print()
                # print(digits, "digitS")
            elif (curr[letter + 1]).isdigit():
                # print(curr[letter + 2], "letter + 2", curr[letter + 1], curr[letter])
                digits = 2
                # print(int(curr[letter] + curr[letter + 1]))
            else:
                digits = 1
                
            special_next = False
            special_above = False
            if digits == 3:
                if letter + 4 < len(curr):
                    temp = letter + 4
                elif letter + 3 < len(curr):
                    temp = letter + 3
                elif letter + 2 < len(curr):
                    temp = letter + 2
                else:
                    temp = letter
                next_line = [new[a] for a in range((letter - 1 if (letter - 1) > 0 else letter - 1), (temp))]
                # print(next_line, "next")
                for b in special_chacters:
                    if b in next_line:
                        special_next = True
                below_line = [before[a] for a in range((letter - 1 if (letter -1 ) > 0 else letter - 1), (temp))]
                for b in special_chacters:
                    if b in below_line:
                        special_above = True
                        # print("MADE IT TRUE", b, below_line)
                        
                
                if ((curr[letter - 1 if letter - 1 > 0 else letter] in special_chacters) or (curr[temp - 1] in special_chacters) or special_next == True or special_above == True):
                    if "*" in curr[letter - 1]
                    
                    total += int(curr[letter] + curr[letter + 1] + curr[letter + 2]) 
                    # print(next_line, "\n", below_line)
                    # print(total, "PASS")
                    # print(True if curr[letter - 1 if letter - 1 > 0 else letter] in special_chacters else False)
                    # print(True if curr[temp] in special_chacters else False)
                    # print(True if special_next == True or special_above == True else False)
                    # print(special_next, next_line)
                    # print(special_above, below_line)
                else:
                    print(curr[letter], letter, "letter", f"c == {c}", f"mod == {mod}")
                    # print(curr[letter - 1], curr[temp], "curr")
                    print(next_line, "\n", below_line)
                    print(total, "FAIL", int(curr[letter] + curr[letter + 1] + curr[letter + 2]) )
                # print(curr[letter - 1], curr[temp], "curr", temp)
                
            elif digits == 2:
                if letter + 3 < len(curr):
                    temp = letter + 3
                elif letter + 2 < len(curr):
                    temp = letter + 2
                
                else:
                    temp = letter
                next_line = [new[a] for a in range((letter - 1 if (letter - 1) > 0 else letter - 1), (temp))]
                # print(next_line, "next")
                for b in special_chacters:
                    if b in next_line:
                        special_next = True
                below_line = [before[a] for a in range((letter - 1 if (letter -1 ) > 0 else letter - 1), (temp))]
                for b in special_chacters:
                    if b in below_line:
                        special_above = True
                        # print("MADE IT TRUE", b, below_line)      
                if (curr[letter - 1] in special_chacters or curr[temp - 1] in special_chacters or special_next == True or special_above == True):
                    total += int(curr[letter] + curr[letter + 1]) 
                    # print(next_line, "\n", below_line)
                else:
                    print(next_line, "\n", below_line)
                    print(total, "FAIL", int(curr[letter] + curr[letter + 1]) )
                    # print(next_line, "\n", below_line)
                # print(total, "total")
            elif digits == 1:
                if letter + 2 < len(curr):
                    temp = letter + 2
                
                else:
                    temp = letter + 1
                next_line = [new[a] for a in range((letter - 1 if (letter - 1) > 0 else letter - 1), (letter + 2 if (letter -1 ) < len(new) else letter + 1))]
                for b in special_chacters:
                    if b in next_line:
                        special_next = True
                below_line = [before[a] for a in range((letter - 1 if (letter -1 ) > 0 else letter - 1), (letter + 2 if (letter -1 ) < len(before) else letter + 1))]
                for b in special_chacters:
                    if b in below_line:
                        special_above = True        
                if (curr[letter - 1] in special_chacters or curr[letter + 1] in special_chacters or special_next == True or special_above == True):
                    total += int(curr[letter]) 
                    print(next_line, "\n", below_line)
                else:
                    print(next_line, "\n", below_line)
                    print(total, "FAIL", int(curr[letter]) )
                print(total, "total")
            special_next = False
            special_above = False
            
            
            if digits == 3: mod += 2
            elif digits == 2: mod += 1
            else: mod += 0
        else:
            if digits == 3: mod += 2
            elif digits == 2: mod += 1
            else: mod += 0               
    count += 1
print(total)              