questions = [
    {
        "question": "Земля плоская?",
        "answer": False
    },
    {
        "question": "Солнце вращается вокруг Земли?",
        "answer": False
    },
    {
        "question": "Вода кипит при температуре 100 градусов Цельсия?",
        "answer": True
    },
    {
        "question": "Коала - медведь?",
        "answer": False
    },
    {
        "question": "Москва - столица России?",
        "answer": True
    }
]

def play_game():
    score = 0
    for question in questions:
        user_answer = input(question["question"] + " (да/нет): ")
        if user_answer.lower() == "да" and question["answer"] or user_answer.lower() == "нет" and not question["answer"]:
            score += 1
            print("Правильно!")
        else:
            print("Неправильно!")
            restart = input("Хотите начать игру сначала? (да/нет): ")
            if restart.lower() == "да":
                play_game()
            else:
                print("Игра завершена.")
                return
    print("Вы ответили правильно на все вопросы! Ваш счет:", score)

play_game()