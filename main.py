import random
import tkinter as tk
import ttkbootstrap as ttk
import os
import sys

player1_score = 0
player2_score = 0
player_decision = 1
wining_score = 25

# game
def rollDice():
        dice_var.set(random.randint(1, 6))
        if dice_var.get() != 1:
            turn_score_var.set(turn_score_var.get() + dice_var.get())
        else:
            changeTurn()


def endTurn():
    global player1_score
    global player2_score
    if player_name.get() == "player 1":

        player1_score += turn_score_var.get()
        if player1_score > wining_score:
            win("player 1")
        else:
            changeTurn()
    else:
        player2_score += turn_score_var.get()
        if player2_score > wining_score:
            win("player 2")
        else:
            changeTurn()

def changeTurn():
    turn_score_var.set(0)
    if player_name.get() == "player 1":
        player_name.set("player 2")
    else:
        player_name.set("player 1")

def win(player):
    win_message_var.set(player + " wins the game!!")
    roll_button.config(state='disabled')
    end_turn_button.config(state='disabled')



# window
window = ttk.Window(themename="darkly")
window.title("Pig")
window.geometry("400x300")
window.resizable(False, False)

# window Icon
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder '_MEIPASS' during one-file execution.
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
icon_path = resource_path("pigIcon.png")
window.iconphoto(False, tk.PhotoImage(file=icon_path))



# tk var
player_name = tk.StringVar(value='player 1')
turn_score_var = tk.IntVar()
dice_var = tk.IntVar()
win_message_var = tk.StringVar()

# widgets

# player
player_title = ttk.Label(master=window, text="hello", font="calibre 24", textvariable=player_name, )
player_title.pack()

# score
score_frame = ttk.Frame(master=window)
turn_score_label = ttk.Label(master=score_frame, font="calibre 24", text="turn score:")
turn_score = ttk.Label(master=score_frame, font="calibre 24", textvariable=turn_score_var)

turn_score_label.pack(side='left')
turn_score.pack(side='left')
score_frame.pack()

#dice
dice_frame = ttk.Frame(master=window)
dice_label = ttk.Label(master=dice_frame, font='calibre 24', text='dice:')
dice = ttk.Label(master=dice_frame, font="calibre 24", textvariable=dice_var)

dice_label.pack(side='left')
dice.pack(side='left')
dice_frame.pack(pady=10)

# win message
win_message = ttk.Label(master=window, font="calibre 24", textvariable=win_message_var)
win_message.pack(pady=20)

#buttons
button_frame = ttk.Frame(master=window)
roll_button = ttk.Button(master=button_frame, text="roll", command=rollDice, width=20)
end_turn_button = ttk.Button(master=button_frame, text="end turn", command=endTurn, width=20)

roll_button.pack(side='left', padx=20)
end_turn_button.pack(side='left')
button_frame.pack()

# run
window.mainloop()