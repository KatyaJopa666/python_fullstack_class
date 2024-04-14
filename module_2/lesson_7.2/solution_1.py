words: list[str] = input('Введите строку: ').split()

reversed_words: list[str] = [word[::-1] for word in words]

print(' '.join(reversed_words))