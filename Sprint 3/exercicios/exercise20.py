a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in range (len(a)):
    revertIndex = len(a) - 1 - i
    b.append(a[revertIndex])
    
print(b)