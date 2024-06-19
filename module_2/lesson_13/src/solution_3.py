from typing import Callable

cache: dict[tuple, int] = {}

def caching(
           func: Callable[[str, str], int],
           cache: dict[tuple, int] = cache
           ) -> Callable[[str, str], None]:
    def cacher(project: str, company_type: str) -> None:
        if (project, company_type) in cache:
            print(f'Загрузили из кеша: {cache[(project, company_type)]}')
        else:
            cache[(project, company_type)] = func(project, company_type)
            print(f'Посчитали цену: {cache[(project, company_type)]}')
    return cacher


@caching
def calculate_project_costs (project: str, company_type: str) -> int:
    if project == 'Логотип' and company_type == 'Малый бизнес':
        return 3000


calculate_project_costs('Логотип', 'Малый бизнес')
calculate_project_costs('Логотип', 'Малый бизнес')