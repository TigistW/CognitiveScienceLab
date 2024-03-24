import tkinter as tk
import random
from tkinter import messagebox
import time

def generate_color_sequence(length):
    sequence = []
    while len(sequence) < length:
        if len(sequence) == 4:
            sequence.append(sequence[3])
        col = random.choice(colors)
        if col not in sequence:
            sequence.append(col)
    return sequence

def generate_hint_color():
    
    hint_color = random.choices(colors, k = 1)
    return hint_color
    
def button_click(color, hint_col):
    global correct_count, incorrect_count, loop_counter, start_time
    
    if color == hint_col[0]:
        result_label.config(text="Correct guess!")
        correct_count += 1
        correct_count_label.config(text=f"Correct: {correct_count}")
        
    else:
        result_label.config(text="Incorrect guess. Try again.")
        incorrect_count += 1
        incorrect_count_label.config(text=f"Incorrect: {incorrect_count}")
        
    sequence = generate_color_sequence(9)
    hint_color = generate_hint_color()
    update_buttons(sequence, hint_color)
    
    loop_counter += 1
    if loop_counter >= 10:
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)
        show_final_message(elapsed_time)
        
def show_final_message(elapsed_time):
    message = f"Game Over!\nCorrect: {correct_count}\nIncorrect: {incorrect_count}\nElapsed Time: {elapsed_time} seconds"
    messagebox.showinfo("Final Result", message)
    root.destroy()

def update_buttons(colors, hint_col):
 
    for i, color in enumerate(colors):
        if i != 4:
            buttons[i].configure(bg=color, command=lambda c=color: button_click(c, hint_col))
    buttons[4].configure(bg=hint_col, state=tk.DISABLED)
    
def create_buttons(root, colors, hint_col):
    buttons = []
    for i, color in enumerate(colors):
        if i == 4:
            button = tk.Button(root, bg = hint_col , width=5, height=2, state=tk.DISABLED)
        else:
            button = tk.Button(root, bg=color, width=10, height=5)
            button.configure(command=lambda c=color: button_click(c, hint_col))
        button.grid(row=i // 3, column=i % 3)
        buttons.append(button)
    return buttons

colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "white"]
sequence = generate_color_sequence(9)
hint_color = generate_hint_color()

root = tk.Tk()
root.title("Color Sequence Game")

buttons = create_buttons(root, sequence, hint_color)
result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=3, rowspan=2)

correct_count = 0
incorrect_count = 0
loop_counter = 0
start_time = time.time()

correct_count_label = tk.Label(root, text="Correct: 0")
correct_count_label.grid(row=5, column=0)
incorrect_count_label = tk.Label(root, text="Incorrect: 0")
incorrect_count_label.grid(row=5, column=2)

root.mainloop()