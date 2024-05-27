from typing import Callable

def collect_data(raw_data: list[int]) -> Callable[[list[int]], Callable[[str], None]]:
    return process_data(raw_data)


def process_data(data: list[int]) -> Callable[[str], None]:
    average: int = str(sum(data) / len(data)).strip('.0')
    return summarize_data(average)


def summarize_data(result: str) -> None:
    print(f'Итог: Среднее значение: {result}')

    
collect_data([1, 2, 3, 4, 5])
collect_data([10, 15, 5, 20])