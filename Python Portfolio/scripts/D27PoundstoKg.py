from tkinter import *


def converter():
    pounds=float(inp.get())
    kg=pounds*0.45359237
    label3.config(text=f"{kg}")

window=Tk()
window.title("Convert MIles to Kms")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)


inp=Entry(width=20)
inp.grid(column=1, row=0)


labell=Label(text="Pounds")
labell.grid(column=2, row=0)

label2=Label(text='is equal to')
label2.grid(column=0, row=1)

label3=Label(text='0')
label3.grid(column=1, row=1)

label4=Label(text='Kgs')
label4.grid(column=2, row=1)

butt=Button(text="Calculate", command=converter)
butt.grid(column=1, row=2)

window.mainloop()