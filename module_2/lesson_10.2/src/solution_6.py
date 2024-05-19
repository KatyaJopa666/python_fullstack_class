def find_max_price(prices: list[str]):
    if len(prices) > 1:
        if prices[0] >= prices[-1]:
            prices.pop()
        else:
            prices.pop(0)
        find_max_price(prices)        
    else:
        print(prices[0])

find_max_price([15, 7, 9])
find_max_price([1, 10, 20, 5])
find_max_price([25, 25, 25])
find_max_price([10, 8, 12])