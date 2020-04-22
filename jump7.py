b = 0
while b <100:
    b = b + 1
    if b % 7 == 0 or b % 10 == 7 or b // 10 == 7:
        continue
    else:
        print(b)
