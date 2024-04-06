products = [1, 14, 4, 8, 6, 9]

def wtf(incoming):
    sum = 0
    for i in incoming:
        sum += i
    return sum

print(wtf(products))