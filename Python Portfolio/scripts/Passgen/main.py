from tkinter import *
from tkinter import messagebox
import task
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genpass():
    fin=task.passgen()
    # fin=task.final_password
    passinp.insert(0, fin)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(passinp.get())==0 or len(webinp.get())==0:
        messagebox.askretrycancel(title="Warning", message="Dont leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=webinp.get(), message=f"Is it ok to save?")
        if is_ok:
            with open("Project 29/passwords.txt", mode='a') as file:
                file.write(f"{webinp.get()}| {eminp.get()} | {passinp.get()}\n")
            webinp.delete(first=0, last=END)
            # eminp.delete(0, END)
            passinp.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, width=400, height=200)



canvas=Canvas(width=200, height=200)
pi=PhotoImage(file=r"D:\USER MATERIAL\Programs\PYTHON PROJECTS\Project 29\logo.png")
canvas.create_image(100,96, image=pi)
canvas.grid(column=1, row=0)


websit=Label(text='Website:')
websit.grid(column=0, row=1)

webinp=Entry(width=52)
webinp.grid(column=1, row=1, columnspan=2)
webinp.focus()

email=Label(text="Email/Username:")
email.grid(column=0, row=2)


eminp=Entry(width=52)
eminp.grid(column=1, row=2, columnspan=2)
eminp.insert(0, 'amir@gmail.com')

password=Label(text="Password:")
password.grid(column=0, row=3)

passinp=Entry(width=34)
passinp.grid(column=1, row=3)

generate=Button(text="Generate Password", command=genpass)
generate.grid(column=2, row=3)

add=Button(text="Add", width=45, command=save)
add.grid(column=1, row=4, columnspan=2)









window.mainloop()