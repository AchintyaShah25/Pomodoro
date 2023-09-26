import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
time = NONE
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global rep
    root.after_cancel(time)
    rep=0
    title["text"]="Timer"
    canvas.itemconfig(timer_text, text=f"{math.floor(WORK_MIN)}:00")
    label2["text"]=""
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global rep
    rep += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if rep %2 !=0:
        counter(work_sec)
        title["text"]="Work"
        title["fg"]=GREEN
    elif rep%8==0:
        counter(long_break_sec)
        title["text"]="Long Break"
        title["fg"]=RED
    elif rep%2==0:
        counter(short_break_sec)
        title["text"]="Short Break"
        title["fg"]=PINK
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    global rep
    global time
    sec = count%60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{math.floor(count/60)}:{sec}")
    if count>0:
        time = root.after(1000, counter, count - 1)
    else:
        timer_start()
        if rep%2==0:
            a = math.floor(rep/2)
            label2.config(text="✓"*a)

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Timer")
root.config(padx= 100, pady= 50, bg=YELLOW)
title = Label(root,text="Timer", font=(FONT_NAME, 50, "bold"))
title.config(fg= GREEN)
title.grid(column=2, row=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tom)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
but1 = Button(root, text="Start",command=timer_start, font=(FONT_NAME, 20, "bold"),bg=YELLOW, fg=GREEN, highlightthickness=0, border=0)
but1.grid(row=3, column=1)
but2 = Button(root, text="Reset",command=reset, font=(FONT_NAME, 20, "bold"),bg=YELLOW, fg=GREEN, highlightthickness=0, border=0)
but2.grid(row=3, column=3)
label2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME,20, "bold"), highlightthickness=0)
label2.grid(row=4, column=2)
root.mainloop()
