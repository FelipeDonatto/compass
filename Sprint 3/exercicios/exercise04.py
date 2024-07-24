for i in range(101):
    divisibleBy = 0;
    for i2 in range (1, i):
        if i % i2 == 0:
            divisibleBy += 1
    if divisibleBy == 1:
        print(i)