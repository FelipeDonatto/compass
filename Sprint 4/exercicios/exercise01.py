file = open("./number.txt")
lines = file.readlines()
numbers = sorted(list(map(lambda x: int(x.strip("\n")), lines)), reverse=True)[:10]
five_evens = list(filter(lambda x: x % 2 == 0, numbers))
print(five_evens)
print(sum(five_evens))
