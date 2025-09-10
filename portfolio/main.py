import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import threading

# ====== SETTINGS ======
SCRIPTS = {
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

BG_COLOR = "#2b2b2b"  # Dark background
FG_COLOR = "#ffffff"  # White text
BUTTON_COLOR = "#444444"
HIGHLIGHT_COLOR = "#00bfff"

# ====== FUNCTIONS ======
def run_script(script_path):
    output_text.delete(1.0, tk.END)  # Clear old output
    status_label.config(text="Running...", fg=HIGHLIGHT_COLOR)

    def execute():
        if os.path.exists(script_path):
            process = subprocess.Popen(
                ["python", script_path],
                text=True,
                # creationflags=subprocess.CREATE_NO_WINDOW,  # No terminal window
                cwd=os.path.dirname(script_path)
            )
            stdout, stderr = process.communicate()
            if stdout:
                output_text.insert(tk.END, stdout)
            if stderr:
                output_text.insert(tk.END, "\nERROR:\n" + stderr)
        else:
            messagebox.showerror("Error", f"Script not found: {script_path}")

        status_label.config(text="Done", fg="#32CD32")

    threading.Thread(target=execute, daemon=True).start()

# ====== MAIN WINDOW ======
root = tk.Tk()
root.title("My Python Portfolio")
root.geometry("700x500")
root.config(bg=BG_COLOR)

# ====== TITLE ======
title_label = tk.Label(root, text="My Python Projects", font=("Arial", 18, "bold"), bg=BG_COLOR, fg=HIGHLIGHT_COLOR)
title_label.pack(pady=10)

# ====== FRAME FOR PROJECT BUTTONS (SCROLLABLE) ======
frame_container = tk.Frame(root, bg=BG_COLOR)
frame_container.pack(pady=10, fill="x")

canvas = tk.Canvas(frame_container, bg=BG_COLOR, highlightthickness=0)
scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add project buttons
for name, path in SCRIPTS.items():
    btn = tk.Button(scrollable_frame, text=name, width=30, bg=BUTTON_COLOR, fg=FG_COLOR,
                    font=("Arial", 12), command=lambda p=path: run_script(p))
    btn.pack(pady=5, padx=10)

# ====== STATUS LABEL ======
status_label = tk.Label(root, text="Ready", font=("Arial", 12), bg=BG_COLOR, fg="#32CD32")
status_label.pack(pady=5)

# ====== OUTPUT BOX ======
output_label = tk.Label(root, text="Output", font=("Arial", 14, "bold"), bg=BG_COLOR, fg=FG_COLOR)
output_label.pack(pady=5)

output_text = tk.Text(root, height=10, width=80, wrap="word", bg="#1e1e1e", fg=FG_COLOR, insertbackground=FG_COLOR)
output_text.pack(pady=10)

# ====== EXIT BUTTON ======
exit_btn = tk.Button(root, text="Exit", width=20, font=("Arial", 12), bg=BUTTON_COLOR, fg=FG_COLOR, command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()
