from typing import Callable
import time

def timer(func: Callable[[str], None]) -> Callable[[str], None]:
    def executor(task: str) -> None:
        start_time: float = time.time()
        func(task)
        end_time: float = time.time()
        execution_time: float = round(end_time - start_time, 2)
        print(f'Execution: {execution_time:.2f} seconds')
    return executor


@timer
def create_design(project: str) -> None:
    if project == 'Логотип Васильевский рынок':
        time.sleep(2.45)
    elif project == 'Макет сайта Логомашины':
        time.sleep(4.30)


create_design('Логотип Васильевский рынок')
create_design('Макет сайта Логомашины')

    