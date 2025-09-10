from tkinter import *
from tkinter import messagebox
import os, subprocess

scripts= {
    "Tip Calculator": r"C:\Users\moham\Documents\portfolio\scripts\D2Tip Calculator.py",
    "Pizza Maker": r"C:\Users\moham\Documents\portfolio\scripts\D3Pizza.py",
    "Treasure Island": r"C:\Users\moham\Documents\portfolio\scripts\D3TreasureIsland.py",
    "Rock, Paper, Scissor": r"C:\Users\moham\Documents\portfolio\scripts\D4RockPaper.py",
    "Password Generator": r"C:\Users\moham\Documents\portfolio\scripts\D5PasswordGenerator.py",
    "Hangman Game": r"C:\Users\moham\Documents\portfolio\scripts\Hangman\Day7- Hangman.py",
    "Cipher Code": r"C:\Users\moham\Documents\portfolio\scripts\D8CaesarCipher.py",
    "Calculator": r"C:\Users\moham\Documents\portfolio\scripts\D10Calc.py",
    "BlackJack": r"C:\Users\moham\Documents\portfolio\scripts\D11Blackjack.py",
    "Guess the Number": r"C:\Users\moham\Documents\portfolio\scripts\D12NumberGuessing.py",
    "Higher Lower Game": r"C:\Users\moham\Documents\portfolio\scripts\HigherLower\main.py",
    "Coffe Vending Machine": r"C:\Users\moham\Documents\portfolio\scripts\CoffeeMachine\main.py",
    "Random Walk": r"C:\Users\moham\Documents\portfolio\scripts\D18RandomWalk.py",
    "Spirograph": r"C:\Users\moham\Documents\portfolio\scripts\D18Spirograph.py",
    "Hirst Painting": r"C:\Users\moham\Documents\portfolio\scripts\D18Hirst.py",
    "Etch a Sketch": r"C:\Users\moham\Documents\portfolio\scripts\D19EtchASketch.py",
    "Turtle Race": r"C:\Users\moham\Documents\portfolio\scripts\D19Race.py",
    "Snake Game": r"C:\Users\moham\Documents\portfolio\scripts\Snake\main.py",
    "Pong Game": r"C:\Users\moham\Documents\portfolio\scripts\Pong\main.py",
    "Turtle Crossing": r"C:\Users\moham\Documents\portfolio\scripts\Turtle Crossing\main.py",
    "Guess the US states": r"C:\Users\moham\Documents\portfolio\scripts\US States Guess\main.py",
    "Pounds to Kg Converter": r"C:\Users\moham\Documents\portfolio\scripts\D27PoundstoKg.py"
}

def run_script(script):
    output_text.delete(1.0, END)
    process = subprocess.Popen(["python", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    output_text.insert(tk.END, stdout if stdout else "")
    if stderr:
        output_text.insert(tk.END, "\nERROR:\n" + stderr)



tk=Tk()
tk.title("Portfolio")
tk.config(width=500, height=500, bg="#f0f0f0")

title=Label(text="My Python Projects", font=('Arial', 16, 'bold'))
title.pack()

for name, path in scripts.items():
    btn=Button(text=name, width=25, font=("Arial", 12), command=lambda p=path: run_script(p))
    btn.pack()


output_text = Text( height=10, width=70)
output_text.pack(pady=10)




tk.mainloop()