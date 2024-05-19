# def calculate_discount(prices: list[int]):
#     discounted_prices: list[int] = []
#     discounted_prices.append(str(prices[0]))
#     prices_count: int = len(prices)
#     def cycle(i: int):
#         if i < prices_count:
#             discounted_prices.append(str(int(prices[i] - 0.1 * prices[i - 1])))
#             cycle(i + 1)
#         else:
#             print(', '.join(discounted_prices))
#     cycle(1)

# calculate_discount([1000, 2000, 3000, 5000, 10000, 15000])
# calculate_discount([100, 200, 300, 400])
# calculate_discount([50, 100])


def calculate_discount(prices: list[int]) -> str:
    discounted_price: int = prices[-1] - 0.1 * prices[-2]
    prices.pop()
    if len(prices) == 1:
        return str(prices[0])+', '+str(int(discounted_price))
    return calculate_discount(prices) + ', ' + str(int(discounted_price))


print(calculate_discount([1000, 2000, 3000, 5000, 10000, 15000]))
print(calculate_discount([100, 200, 300, 400]))
print(calculate_discount([50, 100]))