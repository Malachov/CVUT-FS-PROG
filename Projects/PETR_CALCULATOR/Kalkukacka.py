import tkinter as tk

LARGE_FONT_S = ("Arial", 26, "bold")
DIG_FONT_S = ("Arial", 24, "bold")
DEF_FONT_S = ("Arial", 20)

BILA_1 = "#F8FAFF"
BILA = "#FFFFFF"
SV_MODRA = "#CCEDFF"
SV_SEDA = "#F5F5F5"
BOARD = "#25265E"

calculation = ""

def add_to_calc(symbol):
    
    global calculation
    calculation +=str(symbol)
    text_res.delete(1.0,"end")
    text_res.insert(1.0, calculation)


def evaluate_calc():

    global calculation
    try:
        calculation = str(eval(calculation))
        text_res.delete(1.0,"end")
        text_res.insert(1.0,calculation)
    except:
        clear_field()
        text_res.insert(1.0,"ERROR")


def clear_field():
    global calculation
    calculation = ""
    text_res.delete(1.0,"end")



root = tk.Tk()
root.title("Kalkulačka")
root.geometry("355x375")
root.resizable(0,0)
#root.maxsize(300, 275)
#root.minsize(300, 275)

text_res = tk.Text(root, height=2, width=19, bg=SV_SEDA, fg=BOARD, font=LARGE_FONT_S)
text_res.grid(columnspan=5, sticky=tk.E)





butt_1 = tk.Button(root, text="1", command=lambda: add_to_calc(1), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_1.grid(row=2, column=1, sticky=tk.NSEW)
butt_2 = tk.Button(root, text="2", command=lambda: add_to_calc(2), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_2.grid(row=2, column=2,sticky=tk.NSEW)
butt_3 = tk.Button(root, text="3", command=lambda: add_to_calc(3), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_3.grid(row=2, column=3,sticky=tk.NSEW)
butt_4 = tk.Button(root, text="4", command=lambda: add_to_calc(4), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_4.grid(row=3, column=1,sticky=tk.NSEW)
butt_5 = tk.Button(root, text="5", command=lambda: add_to_calc(5), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_5.grid(row=3, column=2,sticky=tk.NSEW)
butt_6 = tk.Button(root, text="6", command=lambda: add_to_calc(6), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_6.grid(row=3, column=3,sticky=tk.NSEW)
butt_7 = tk.Button(root, text="7", command=lambda: add_to_calc(7), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_7.grid(row=4, column=1,sticky=tk.NSEW)
butt_8 = tk.Button(root, text="8", command=lambda: add_to_calc(8), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_8.grid(row=4, column=2, sticky=tk.NSEW)
butt_9 = tk.Button(root, text="9", command=lambda: add_to_calc(9), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_9.grid(row=4, column=3,sticky=tk.NSEW)
butt_0 = tk.Button(root, text="0", command=lambda: add_to_calc(0), bg=BILA, fg=BOARD, font=DIG_FONT_S, borderwidth=0)
butt_0.grid(row=5, column=2,sticky=tk.NSEW)

butt_plus = tk.Button(root, text="+", command=lambda: add_to_calc("+"), width=5, bg=BILA_1, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_plus.grid(row=2, column=4,sticky=tk.NSEW)
butt_minus = tk.Button(root, text="-", command=lambda: add_to_calc("-"), width=5, bg=BILA_1, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_minus.grid(row=3, column=4,sticky=tk.NSEW)
butt_multiply = tk.Button(root, text="*", command=lambda: add_to_calc("*"), width=5, bg=BILA_1, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_multiply.grid(row=4, column=4,sticky=tk.NSEW)
butt_division = tk.Button(root, text="/", command=lambda: add_to_calc("/"), width=5, bg=BILA_1, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_division.grid(row=5, column=4,sticky=tk.NSEW)

butt_open = tk.Button(root, text="(", command=lambda: add_to_calc("("), width=5, bg=BILA_1, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_open.grid(row=5, column=1,sticky=tk.NSEW)
butt_close = tk.Button(root, text=")", command=lambda: add_to_calc(")"), width=5, bg=BILA_1, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_close.grid(row=5, column=3,sticky=tk.NSEW)
butt_dott = tk.Button(root, text=".", command=lambda: add_to_calc("."), width=5, bg=BILA_1, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_dott.grid(row=6, column=1,sticky=tk.NSEW)

butt_equals = tk.Button(root, text="=", command=evaluate_calc, width=11, bg=SV_MODRA, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_equals.grid(row=6, column=3, columnspan=2,sticky=tk.NSEW)
butt_clear = tk.Button(root, text="C", command=clear_field, width=5,bg=BILA_1, fg=BOARD, font=DEF_FONT_S, borderwidth=0)
butt_clear.grid(row=6, column=2,sticky=tk.NSEW)


root.mainloop()



