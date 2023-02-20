import pyfiglet
import os

d_en = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
        'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
d_ru = {'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2,
        'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10,
        'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3}


# Функция которая считает количество очков  в слове
def scrabble_game(coll, dict):
    total = 0
    try:
        for i in coll:
            total += dict[i]
        print(f'Your word points are equal: {total}')
    except KeyError:
        print('Word entered incorrectly')


print(pyfiglet.figlet_format('Scrabble Game'))

resert_game = 'r'
while resert_game == 'r':
    os.system('CLS')
    language = input("\n\nSelect language 'ru' or 'en': ").lower()
    word = list(input('Enter your word: ').upper())
# Смотря какую раскладку выбрал игрок берем нужный нам словарь
    if language == 'en':
        scrabble_game(word, d_en)
    elif language == 'ru':
        scrabble_game(word, d_ru)
# Здесь можем начать играть заново или полностью прекратить игру
    resert_game = input('If you want to play again, enter R to end the game, enter Q: ').lower()
    if resert_game == 'q':
        print('Bye!')
        break
