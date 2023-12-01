first_num = 0
second_num = 0
total = 0
for i in range(1000):
    word = input()
    for a in word:
        try:
            first_num = int(a)
            if first_num != 0:
                break
        except:
            pass
    for a in word[::-1]:
        try:
            second_num = int(a)
            if second_num != 0:
                break
        except:
            pass
    num = int(str(first_num) + str(second_num))
    print(num)
    total += num
print(total)