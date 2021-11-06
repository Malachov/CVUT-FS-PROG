import tkinter as tk
import random as rd

players = ['X', 'O']
player = rd.choice(players)

ls_buttons = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]


def btn_press(row_index, col_index):
    global player
    if ls_buttons[row_index][col_index]["text"] == "" and win_check() is not True:
        if player == players[0]:
            ls_buttons[row_index][col_index]["text"] = player
            if win_check():
                lbl_turn.config(text=f"Player [{player}] is WINNER!")
            elif emty_spaces():
                lbl_turn.config(text=f"It's DRAW!")
            else:
                player = players[1]
                lbl_turn.config(text=f"Player [{player}] turn!")
        elif player == players[1]:
            ls_buttons[row_index][col_index]["text"] = player
            if win_check():
                lbl_turn.config(text=f"Player [{player}] is WINNER!")
            elif emty_spaces():
                lbl_turn.config(text=f"It's DRAW!")
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
        if count == 3:
            #print("sm is winner H")
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
        #print("sm is winner D")
        for i in range(3):
            ls_buttons[i][i].config(bg="green")
        return True
    elif ls_buttons[0][2]["text"] == ls_buttons[1][1]["text"] == ls_buttons[2][0]["text"] != "":
        #print("sm is winner D")
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
    player = rd.choice(players)
    lbl_turn.config(text=f"Player [{player}] turn!")
    for r in range(3):
        for c in range(3):
            ls_buttons[r][c].config(text="", bg="#F0F0F0")


# Desktop window
window = tk.Tk()
window.title("Tic - Tac - Toe")

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


window.mainloop()
