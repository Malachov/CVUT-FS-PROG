import tkinter as tk


def btn_press(row_index, col_index):
    ls_buttons[row_index][col_index]["text"] = "It was pressed!"


def new_game():
    for r in range(3):
        for c in range(3):
            ls_buttons[r][c]["text"] = f"[{r};{c}]"


ls_buttons = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]


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
                    text="Player [X,O] turn!")
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
    # ls_buttons.append([])
    for c in range(3):
        ls_buttons[r][c] = tk.Button(master=frm_content,
                                     #font=('consolas', 10),
                                     text=f"[{r};{c}]",
                                     width=5,
                                     height=5,
                                     command=lambda row=r, column=c: btn_press(row, column))
        ls_buttons[r][c].grid(row=r, column=c, sticky="snew")


window.mainloop()
