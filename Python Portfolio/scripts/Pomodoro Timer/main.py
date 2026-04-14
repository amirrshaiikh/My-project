from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
CHECKS="✔" 
timerr=None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetting():
    window.after_cancel(timerr)
    timer.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps=0
    check.config(text='')



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_sec=WORK_MIN*60
    short_sec=SHORT_BREAK_MIN*60
    long_sec=LONG_BREAK_MIN*60
    global reps
    reps+=1
    check.config(text=CHECKS * math.floor(reps/2))
    if reps==1 or reps==3 or reps==5 or reps==7:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)
    elif reps==2 or reps==4 or reps==6:
        count_down(short_sec)
        timer.config(text="Break", fg=PINK)
    elif reps==8:
        count_down(long_sec)
        timer.config(text="Break", fg=RED)
    



    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=round(count%60)
    if count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min<10:
        count_min=f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timerr
        timerr=window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.config(width=300, height=300, bg=YELLOW)
window.title("Pomodoro")
window.config(padx=100, pady=50)

timer=Label(text='Timer', bg=YELLOW,  font=(FONT_NAME, 50, ''), fg=GREEN)
timer.grid(column=1, row=0)


canvas=Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
pi=PhotoImage(file=r"D:\USER MATERIAL\Programs\PYTHON PROJECTS\Project 28\tomato.png")
canvas.create_image(102, 112, image=pi)
timer_text=canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start=Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset=Button(text="Reset", command=resetting)
reset.grid(column=2, row=2)

check=Label(text='', font=(FONT_NAME, 18), bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)



window.mainloop()