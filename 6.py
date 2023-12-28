import random
words = []
for i in range(10):
    word = input(f"Введите слово {i+1}: ")
    words.append(word)
secret_word = random.choice(words)
hint1 = f"Количество букв А и О в искомом слове: {secret_word.count('А') + secret_word.count('О')}"
hint2 = f"2 буквы из слова слева от искомого: {words[words.index(secret_word)-1][-2:]}"
hint3 = f"Длиннее или короче слово справа от искомого: {'длиннее' if len(secret_word) < len(words[words.index(secret_word)+1]) else 'короче'}"
print("Список слов:")
for i, word in enumerate(words):
    print(f"{i+1}: {word}")
print("Подсказки:")
print("Подсказка №1:", hint1)
print("Подсказка №2:", hint2)
print("Подсказка №3:", hint3)
guess = int(input("Введите номер слова, которое вы считаете загаданным: "))
if guess == words.index(secret_word) + 1:
    print("Поздравляем, вы угадали!")
else:
    print("К сожалению, вы не угадали.")
    print("Загаданное слово было под номером", words.index(secret_word) + 1)