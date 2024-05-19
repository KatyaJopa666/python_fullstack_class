def hard_worker(stats: dict[str, int]):
    worker: str = max(stats, key = stats.get)
    max_completed_tasks: int = stats[worker]
    hard_workers_count: int = list(stats.values()).count(max_completed_tasks)
    if hard_workers_count == 1:
        print(stats, f'   Самый ответственный: {worker}')
    else:
        hard_workers: list[str] = [worker for worker in stats if stats[worker] == max_completed_tasks]   
        print(stats, f"   Самый ответственный: {', '.join(hard_workers)}")

hard_worker({'Анна': 5, 'Боб': 7, 'Сюзан': 9})
hard_worker({'Джон': 1, 'Майк': 1, 'Эмили': 1})