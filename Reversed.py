def chappa_1(arrayjon):
    arr = [] # local variable
    n = len(arrayjon)
    for i in range(n):
        index = (n-1) - i
        a = arrayjon[index]
        arr.append(a)
    return arr

def chappa_2(arrayjon):
    arr = []
    for el in reversed(arrayjon):
        arr.append(el)
    return arr

nums = [4, 6, 7, 13, 5, 9, 7, 2, 3, 25]
result = chappa_1(nums)
print(result)






