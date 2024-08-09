def pares_ate(n:int):
    nums = []
    for i in range(2,n+1):
        if i % 2 == 0:
            nums.append(i)
            print(nums)
            yield i

