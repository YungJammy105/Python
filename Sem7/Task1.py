song = input('введите тестовую фразу\n').split()
list_len = []
open_voice = "аяуюоеёэиы"

for phrase in song:
    list_vowels = [vowels for vowels in phrase if vowels in open_voice]
    list_len.append(len(list_vowels))

print("Парам пам-пам" if len(set(list_len)) == 1 else "Пам парам")