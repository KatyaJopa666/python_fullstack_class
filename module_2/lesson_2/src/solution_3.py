BOOK_VOLUME: float = 2
STATIONARY_VOLUME: float = 1.5
TOY_VOLUME: float = 3

books = int(input('Количество книг: '))
stationery = int(input('Количество канцтоваров: '))
toys = int(input('Количество игрушек: '))

total_volume: float = BOOK_VOLUME*books + STATIONARY_VOLUME*stationery + TOY_VOLUME*toys
print('Общий объём:', total_volume, 'м^3')