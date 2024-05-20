def sales_shedule_with_range(days) -> None:
    sale_days: list[int] = [day for day in range(3, days + 1, 3)]
    print(sale_days)


sales_shedule_with_range(30)
sales_shedule_with_range(31)


    