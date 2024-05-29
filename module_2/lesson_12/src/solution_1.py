from statistics import mean

def collect_data(raw_data: list[int]) -> None:
    process_data(raw_data)


def process_data(data: list[int]) -> None:
    average: float = mean(data)
    summarize_data(average)


def summarize_data(result: float) -> None:
    print(f'Итог: Среднее значение: {result}')

    
collect_data([1, 2, 3, 4, 5])
collect_data([10, 15, 5, 20])