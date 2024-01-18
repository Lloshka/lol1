import random
from tkinter import *

def generate_random_number_1_to_6():
    random_number = random.randint(1, 6)
    result_text.delete('1.0', END)
    result_text.insert(END, str(random_number))

def generate_random_number_1_to_20():
    random_number = random.randint(1, 20)
    result_text.delete('1.0', END)
    result_text.insert(END, str(random_number))

root = Tk()
root.title("Random Number Generator")

text_frame = Frame(root)
text_frame.pack()

result_text = Text(text_frame, height=1, width=10)
result_text.pack()

button_frame = Frame(root)
button_frame.pack()

button_1_to_6 = Button(button_frame, text="1 to 6", command=generate_random_number_1_to_6)
button_1_to_6.pack(side=LEFT)

button_1_to_20 = Button(button_frame, text="1 to 20", command=generate_random_number_1_to_20)
button_1_to_20.pack(side=LEFT)

root.mainloop()