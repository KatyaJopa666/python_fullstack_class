def background_color(hour: int) -> str:
    color: str = 'Тёмный'
    if 6 <= hour < 18:
        color = 'Светлый'
    print(f'Текущее время: {hour}    Цвет фона: {color}')

background_color(10)
background_color(20)
background_color(5)
