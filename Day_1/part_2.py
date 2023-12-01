first_num, second_num, total = 0, 0, 0
nums = "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split()

for i in range(1000):
    word = input()
    curr_list, new_list = list(), list()
    for a in nums:
        try:
            if word.count(a) > 1:
                curr_list.append(word.rfind(a))
                new_list.append(a)
                curr_list.append(word.find(a))
                new_list.append(a)
            else:
                curr_list.append(word.index(a))
                new_list.append(a)
        except:
            pass
    
    first_word = new_list[curr_list.index(min(curr_list))]
    second_word = new_list[curr_list.index(max(curr_list))]

    if first_word == "one":
        first_word = "1"
    elif first_word == "two":
        first_word = "2"
    elif first_word == "three":
        first_word = "3"
    elif first_word == "four":
        first_word = "4"
    if first_word == "five":
        first_word = "5"
    elif first_word == "six":
        first_word = "6"
    if first_word == "seven":
        first_word = "7"
    elif first_word == "eight":
        first_word = "8"
    elif first_word == "nine":
        first_word = "9"
    else:
        pass
        
    if second_word == "one":
        second_word = "1"
    elif second_word == "two":
        second_word = "2"
    elif second_word == "three":
        second_word = "3"
    elif second_word == "four":
        second_word = "4"
    if second_word == "five":
        second_word = "5"
    elif second_word == "six":
        second_word = "6"
    if second_word == "seven":
        second_word = "7"
    elif second_word == "eight":
        second_word = "8"
    elif second_word == "nine":
        second_word = "9"
    else:
        pass

    total += int(str(first_word) + str(second_word))
print(total)