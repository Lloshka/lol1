import random
dict_triggers = {
"привет": ["Привет!", "Здравствуйте!"],
"как дела": ["Хорошо, спасибо!", "Всё отлично, а у вас?"],
"что делаешь": ["Отвечаю на вопросы :)", "Работаю над задачей."],
"пока": ["До свидания!", "Удачного дня!"]
}

exit_trigger = "пока"

while True:
    user_input = input("Введите сообщение: ")
    if user_input.lower() in dict_triggers:
        computer_response = dict_triggers[user_input.lower()][random.randint(0, len(dict_triggers[user_input.lower()])-1)]
        print(computer_response)
    
        if user_input.lower() == exit_trigger:
            break
    else:
        print("Извините, я не понял ваш вопрос. Попробуйте еще раз.")
