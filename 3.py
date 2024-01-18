from tkinter import *

def change_color(color):
    gray_button.configure(bg=color)

def gray_button_clicked():
    gray_button.configure(bg="gray")

root = Tk()
root.title("Изменение цвета кнопок")

# Создание кнопок цветов радуги
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
rainbow_buttons = []
for color in rainbow_colors:
    button = Button(root,width=12, bg=color, command=lambda c=color: change_color(c))
    button.pack()
    rainbow_buttons.append(button)

# Создание серой кнопки
gray_button = Button(root,width=12, bg="gray", command=gray_button_clicked)
gray_button.pack()

root.mainloop()