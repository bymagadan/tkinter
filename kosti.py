import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=str(result))

root = tk.Tk()
root.title("Бросаем игровые кости в Tkinter :) ")

result_label = tk.Label(root, text="")
result_label.pack()

roll_button = tk.Button(root, text="Бросить", command=roll_dice)
roll_button.pack()

root.mainloop()
