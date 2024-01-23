import re
def check_name(name):
    # Проверка написания с заглавной буквы
    if not name[0].isupper():
        return False
    
    # Проверка на наличие цифр
    if re.search(r'\d', name):
        return False
    
    # Проверка на наличие запрещенных символов
    if re.search(r'[!?\.\n,:;+*/]', name):
        return False
    
    # Проверка на наличие пробелов
    if ' ' in name:
        return False
    
    return True
name = input("Введите имя: ")
if check_name(name):
    print("Имя введено правильно.")
else:
    print("Имя введено неправильно.")