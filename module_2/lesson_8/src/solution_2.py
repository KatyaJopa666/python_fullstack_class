synonyms: dict[str, str] = {'Красивый':'Прекрасный', 'Уродливый':'Некрасивый', 'Сложный':'Запутанный', 'Простой':'Лёгкий'}

def go():
    word: str = input('Введите слово: ')
    if word in synonyms:
        print(f'Синоним: {synonyms[word]}')
    else:
        synonyms[word] = input('Такого слова ещё нет в словаре. Введите синоним для него: ')
    go()
go()