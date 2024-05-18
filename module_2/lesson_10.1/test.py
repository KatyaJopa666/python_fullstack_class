# print([] and 1 or 6)
# x: int = 0
# print(-3 < x < 10)

def recursion(fu):
    if fu >= 0:
        fu -= 1
        print(fu)
        recursion(fu)
    else:
        print(fu)
    


recursion(10)