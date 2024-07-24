def somaString(string): 
    nums = string.split(",")
    total = 0
    for i in nums:
        total += int(i)
    print(total)
    
somaString("1,3,4,6,10,76")