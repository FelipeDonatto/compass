def my_map(list, f):
    newList = []
    for item in list:
        newList.append(f(item))
    print(newList)


def df(x):
    return x**2


my_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], df) 