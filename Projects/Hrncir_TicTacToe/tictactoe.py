import tkinter as tk
import random as rd
import playersAI

WINSIZE = 3


def get_board(buttons):
    board = []
    for r in buttons:
        row = []
        for btn in r:
            row.append(btn["text"])
        board.append(row)
    return board


def btn_press(row_index, col_index):
    global player
    if ls_buttons[row_index][col_index]["text"] == "" and win_check() is not True:
        if player == players[0]:
            ls_buttons[row_index][col_index]["text"] = player
            if win_check():
                lbl_turn.config(text=f"Player [{player}] is WINNER!")
            elif emty_spaces():
                lbl_turn.config(text=f"It's DRAW!")
            elif aiSwitch == True:
                moveAI = playerAI.move(get_board(ls_buttons))
                ls_buttons[moveAI[0]][moveAI[1]]["text"] = players[1]
                if win_check():
                    lbl_turn.config(text=f"Player [{players[1]}] is WINNER!")
            else:
                player = players[1]
                lbl_turn.config(text=f"Player [{player}] turn!")
        elif player == players[1]:
            ls_buttons[row_index][col_index]["text"] = player
            if win_check():
                lbl_turn.config(text=f"Player [{player}] is WINNER!")
            elif emty_spaces():
                lbl_turn.config(text=f"It's DRAW!")
            elif aiSwitch == True:
                moveAI = playerAI.move(get_board(ls_buttons))
                ls_buttons[moveAI[0]][moveAI[1]]["text"] = players[0]
                if win_check():
                    lbl_turn.config(text=f"Player [{players[0]}] is WINNER!")
            else:
                player = players[0]
                lbl_turn.config(text=f"Player [{player}] turn!")


def check_list(data):
    for r in data:
        count = 0
        first_btn = r[0]["text"]
        for button in r:
            if first_btn == button["text"] and first_btn != "":
                count += 1
        if count == WINSIZE:
            for btn in r:
                btn.config(bg="green")
            return True
    return False


def win_check():
    # horizontal
    if check_list(ls_buttons):
        return True
    # vertical
    column = []
    col0 = []
    col2 = []
    col1 = []
    for row in ls_buttons:
        col0.append(row[0])
        col1.append(row[1])
        col2.append(row[2])
    column.append(col0)
    column.append(col1)
    column.append(col2)
    if check_list(column):
        return True
    # diagonal
    elif ls_buttons[0][0]["text"] == ls_buttons[1][1]["text"] == ls_buttons[2][2]["text"] != "":
        for i in range(3):
            ls_buttons[i][i].config(bg="green")
        return True
    elif ls_buttons[0][2]["text"] == ls_buttons[1][1]["text"] == ls_buttons[2][0]["text"] != "":
        for i, j in zip(range(0, 3), range(2, -1, -1)):
            ls_buttons[i][j].config(bg="green")
        return True
    else:
        return False


def emty_spaces():
    emty = 9
    for row in ls_buttons:
        for btn in row:
            if btn["text"] != "":
                emty -= 1
    if emty == 0:
        return True
    else:
        return False


def new_game():
    global player
    if aiSwitch == False:
        player = rd.choice(players)
    elif aiSwitch == True:
        player = players[0]
    lbl_turn.config(text=f"Player [{player}] turn!")
    for r in range(3):
        for c in range(3):
            ls_buttons[r][c].config(text="", bg="#F0F0F0")
    if aiStart == True:
        ls_buttons[rd.randint(0, 2)][rd.randint(0, 2)]["text"] = players[1]


def ai_settings():
    global aiSwitch, playerAI
    if aiSwitch == False:
        option = value_inside.get()
        for i in range(len(ls_playersAI)):
            if option == options_list[i]:
                playerAI = ls_playersAI[i]
                aiSwitch = True
                new_game()
                btn_AI_on_off.config(text="OFF")
    elif aiSwitch == True:
        aiSwitch = False
        new_game()
        btn_AI_on_off.config(text="ON")
        value_inside.set("AI settings:")


def who_start():
    global aiStart
    if aiStart == False:
        aiStart = True
        btn_who_first.config(text="AI starts!")
    else:
        aiStart = False
        btn_who_first.config(text="You starts!")


players = ['X', 'O']
player = players[0]
# AI
aiSwitch = False
pEasy = playersAI.Player('O', 'X')
pMedium = playersAI.PlayerMax('O', 'X')
pHard = playersAI.PlayerBlocker('O', 'X')
pExtreme = playersAI.PlayerMinimax('O', 'X')
ls_playersAI = [pEasy, pMedium, pHard, pExtreme]
playerAI = ls_playersAI[1]

ls_buttons = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
# player/AI start
aiStart = False

# Desktop window
window = tk.Tk()
window.title("Tic - Tac - Toe")
# window.iconbitmap('myicon.ico')

# Menu
lbl_title = tk.Label(master=window,
                     font=('consolas', 20),
                     text="Tic - Tac - Toe", relief=tk.RAISED, borderwidth=5)
lbl_title.pack(fill=tk.BOTH, side=tk.TOP, expand=False)
frm_menu = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frm_menu.pack(fill=tk.X, side=tk.TOP, expand=False)
frm_menu.columnconfigure([0, 1], weight=20, minsize=50)
frm_menu.rowconfigure(1, weight=1, minsize=50)
lbl_turn = tk.Label(master=frm_menu,
                    font=('consolas', 10),
                    text=f"Player [{player}] turn!")
btn_restart = tk.Button(master=frm_menu,
                        font=('consolas', 10),
                        text="Restart",
                        command=new_game)

lbl_turn.grid(row=1, column=0, sticky="snew")
btn_restart.grid(row=1, column=1, sticky="snew")

# PlayField
frm_content = tk.Frame(master=window, bg="blue")
frm_content.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

for r in range(3):
    frm_content.columnconfigure(r, weight=20, minsize=50)
    frm_content.rowconfigure(r, weight=1, minsize=50)
    for c in range(3):
        ls_buttons[r][c] = tk.Button(master=frm_content,
                                     #font=('consolas', 10),
                                     text="",
                                     width=5,
                                     height=5,
                                     command=lambda row=r, column=c: btn_press(row, column))
        ls_buttons[r][c].grid(row=r, column=c, sticky="snew")

# AI setting
frm_footer = tk.Frame(master=window)
frm_footer.rowconfigure(0, weight=1, minsize=10)
frm_footer.columnconfigure([0, 1, 2], weight=20, minsize=10)
frm_footer.pack(fill=tk.BOTH, side=tk.TOP)
options_list = ["Easy", "Medium", "Hard", "Extreme"]
value_inside = tk.StringVar(master=frm_footer)
value_inside.set("Settings AI:")
option_AI = tk.OptionMenu(frm_footer, value_inside, *options_list)
option_AI.grid(row=0, column=0, sticky="w")
btn_who_first = tk.Button(
    master=frm_footer, text="You starts!", command=who_start)
btn_who_first.grid(row=0, column=1, padx=5, pady=5, sticky="e")
btn_AI_on_off = tk.Button(master=frm_footer, text="ON", command=ai_settings)
btn_AI_on_off.grid(row=0, column=2, padx=5, pady=5, sticky="e")


window.mainloop()
