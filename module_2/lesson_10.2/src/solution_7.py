def calculate_discount(prices: list[int]):
    discounted_prices: list[int] = []
    discounted_prices.append(str(prices[0]))
    prices_count: int = len(prices)
    def cycle(i: int):
        if i < prices_count:
            discounted_prices.append(str(int(prices[i] - 0.1 * prices[i - 1])))
            cycle(i + 1)
        else:
            print(', '.join(discounted_prices))
    cycle(1)

calculate_discount([1000, 2000, 3000])
calculate_discount([5000, 10000, 15000])
calculate_discount([100, 200, 300, 400])
calculate_discount([50, 100])