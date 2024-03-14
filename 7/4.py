# Открываем файл log.txt для записи и чтения


# Получаем строки, которые пользователь хочет сохранить в записной книжке
def get_notes():
    with open("log.txt", "a+",1, 'UTF-8') as file:
        note = input("Введите строку для записи в записную книжку: ")
        file.write(note + "\n")
        file.close()


# Выводим все строки из записной книжки
def show_all_notes():
    file = open("log.txt", "r", 1, 'UTF-8')
    print("Содержимое записной книжки:")
    print(file.read())
    file.close()

# Выводим указанную строку из записной книжки
def show_specific_note():
    line_number = int(input("Введите номер строки для отображения: "))
    with open("log.txt", "r", 1, 'UTF-8') as file:
        lines = file.readlines()
        if line_number <= len(lines):
            print(lines[line_number - 1])
        else:
            print("Указанной строки не существует")

# Основная программа
def main():
    while True:
        mode = input("Выберите режим (1 - Целый документ, 2 - Указанная строка, 3 - Запись данных,  4 - Для выхода): ")
        if mode == "1":
            show_all_notes()
        elif mode == "2":
            show_specific_note()
        elif mode == '3':
            get_notes()
        elif mode.lower() == "4":
            break
        else:
            print("Неверный режим, попробуйте снова.")

# Запускаем программу
main()