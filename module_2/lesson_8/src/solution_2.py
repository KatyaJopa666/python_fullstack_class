synonyms: dict[str, str] = {'Красивый':'Прекрасный', 'Уродливый':'Некрасивый', 'Сложный':'Запутанный', 'Простой':'Лёгкий'}

synonyms_reversed: dict[str, str] = {value:key for key, value in synonyms.items()}

synonyms.update(synonyms_reversed)

def go():
    word: str = input('Введите слово: ')
    if word in synonyms:
        print(f'Синоним: {synonyms[word]}')
    else:
        synonym: str = input('Такого слова ещё нет в словаре. Введите синоним для него: ')
        synonyms[word], synonyms[synonym] = synonym, word
    go()
go()