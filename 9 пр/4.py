import tkinter as tk

def check_answer(answer):
    if answer == True:
        answer_label.config(text="Верно", bg="green")
    else:
        answer_label.config(text="Неверно", bg="red")

root = tk.Tk()

question_label = tk.Label(root, text="2 + 2 = 4?")
question_label.pack()

answer_label = tk.Label(root, text="")
answer_label.pack()

true_button = tk.Button(root, text="Верно", command=lambda: check_answer(True))
true_button.pack(side=tk.LEFT, padx=(20, 10))

false_button = tk.Button(root, text="Неверно", command=lambda: check_answer(False))
false_button.pack(side=tk.RIGHT, padx=(10, 20))

root.mainloop()