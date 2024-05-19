def analyze_ad_efficiency(clicks: int, shows: int, views: int):
    efficiency = clicks / shows
    if efficiency > 0.1:
        print('Высокая')
    elif 0.1> efficiency > 0.05:
        print('Средняя')
    elif 0.05 > efficiency > 0.01:
        print('Низкая')
    elif efficiency < 0.01:
        print('Недооцененная')
    else:
        print('Неопределенная')

analyze_ad_efficiency(50, 10_000, 15_000)
analyze_ad_efficiency(200, 10_000, 5_000)
analyze_ad_efficiency(700, 10_000, 800)
analyze_ad_efficiency(1_200, 10_000, 1_000)
analyze_ad_efficiency(500, 10_000, 200)