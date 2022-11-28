import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 24, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

calculation = ""

def add_to_calculation(symbol):
    
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():

    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"ERROR")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")



root = tk.Tk()
root.title("Kalkulačka")
root.geometry("355x375")
root.resizable(0,0)
#root.maxsize(300, 275)
#root.minsize(300, 275)

text_result = tk.Text(root, height=2, width=19, bg=LIGHT_GRAY, fg=LABEL_COLOR, font=LARGE_FONT_STYLE)
text_result.grid(columnspan=5, sticky=tk.NSEW)





btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_1.grid(row=2, column=1, sticky=tk.NSEW)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_2.grid(row=2, column=2,sticky=tk.NSEW)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_3.grid(row=2, column=3,sticky=tk.NSEW)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_4.grid(row=3, column=1,sticky=tk.NSEW)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_5.grid(row=3, column=2,sticky=tk.NSEW)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_6.grid(row=3, column=3,sticky=tk.NSEW)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_7.grid(row=4, column=1,sticky=tk.NSEW)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_8.grid(row=4, column=2, sticky=tk.NSEW)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_9.grid(row=4, column=3,sticky=tk.NSEW)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0)
btn_0.grid(row=5, column=2,sticky=tk.NSEW)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_plus.grid(row=2, column=4,sticky=tk.NSEW)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_minus.grid(row=3, column=4,sticky=tk.NSEW)
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_multiply.grid(row=4, column=4,sticky=tk.NSEW)
btn_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_division.grid(row=5, column=4,sticky=tk.NSEW)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_open.grid(row=5, column=1,sticky=tk.NSEW)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_close.grid(row=5, column=3,sticky=tk.NSEW)
btn_dott = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_dott.grid(row=6, column=1,sticky=tk.NSEW)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_equals.grid(row=6, column=3, columnspan=2,sticky=tk.NSEW)
btn_clear = tk.Button(root, text="C", command=clear_field, width=5,bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
btn_clear.grid(row=6, column=2,sticky=tk.NSEW)


root.mainloop()



