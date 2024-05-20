def sum_sales_with_for(sales: list[int]) -> None:
    sales_sum: int = 0
    for sale in sales:
        sales_sum += sale
    print('Сумма продаж: ', end = '')
    print(*sales, sep = '+', end = '=' + str(sales_sum) + '\n')
    
    
sum_sales_with_for([100, 200, 300])
sum_sales_with_for([15, 23, 39, 50])
