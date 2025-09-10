import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import threading
import sys

# Determine base directory depending on execution context
base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# List of script names and relative paths
SCRIPTS = {
    # "Tip Calculator": "scripts/D2TipCalculator.py",
    # "Pizza Maker": "scripts/D3Pizza.py",
    # "Treasure Island": "scripts/D3TreasureIsland.py",
    # "Rock, Paper, Scissor": "scripts/D4RockPaper.py",
    # "Password Generator": "scripts/D5PasswordGenerator.py",
    # "Hangman Game": "scripts/Hangman/Day7- Hangman.py",
    # "Cipher Code": "scripts/D8CaesarCipher.py",
    # "Calculator": "scripts/D10Calc.py",
    # "BlackJack": "scripts/D11Blackjack.py",
    # "Guess the Number": "scripts/D12NumberGuessing.py",
    # "Higher Lower Game": "scripts/HigherLower/main.py",
    # "Coffee Vending Machine": "scripts/CoffeeMachine/main.py",
    "Random Walk": "scripts/D18RandomWalk.py",
    "Spirograph": "scripts/D18Spirograph.py",
    "Hirst Painting": "scripts/D18Hirst.py",
    "Etch a Sketch": "scripts/D19EtchASketch.py",
    "Turtle Race": "scripts/D19Race.py",
    "Snake Game": "scripts/Snake/main.py",
    "Pong Game": "scripts/Pong/main.py",
    "Turtle Crossing": "scripts/TurtleCrossing/main.py",
    "Guess the US states": "scripts/USStatesGuess/main.py",
    "Pounds to Kg Converter": "scripts/D27PoundstoKg.py"
}

# Appearance settings
BG_COLOR = "#2b2b2b"
FG_COLOR = "#ffffff"
BUTTON_COLOR = "#444444"
HIGHLIGHT_COLOR = "#00bfff"
SUCCESS_COLOR = "#32CD32"
ERROR_COLOR = "#ff4c4c"

def run_script(relative_path):
    script_path = os.path.join(base_dir, relative_path)
    output_text.delete(1.0, tk.END)
    status_label.config(text="Running...", fg=HIGHLIGHT_COLOR)

    def execute():
        try:
            if not os.path.exists(script_path):
                raise FileNotFoundError(f"Script not found:\n{script_path}")

            process = subprocess.Popen(
                [sys.executable, script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=os.path.dirname(script_path)
            )
            stdout, stderr = process.communicate()

            if stdout: 
                output_text.insert(tk.END, "Output:\n" + stdout + "\n")
            if stderr:
                output_text.insert(tk.END, "ERROR:\n" + stderr)
                status_label.config(text="Error occurred", fg=ERROR_COLOR)
            else:
                status_label.config(text="Done", fg=SUCCESS_COLOR)

        except Exception as e:
            output_text.insert(tk.END, f"Unexpected error:\n{str(e)}")
            status_label.config(text="Error", fg=ERROR_COLOR)

    threading.Thread(target=execute, daemon=True).start()

# Main window setup
root = tk.Tk()
root.title("Python Projects")
root.geometry("800x600")
root.config(bg=BG_COLOR)

tk.Label(root, text="My Python Projects", font=("Arial", 18, "bold"),
         bg=BG_COLOR, fg=HIGHLIGHT_COLOR).pack(pady=10)

# Scrollable frame for buttons
container = tk.Frame(root, bg=BG_COLOR)
container.pack(fill="both", expand=True, pady=10)

canvas = tk.Canvas(container, bg=BG_COLOR, highlightthickness=0)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

# Add buttons for each script
for name, rel_path in SCRIPTS.items():
    tk.Button(scrollable_frame, text=name, width=40, anchor="w",
              bg=BUTTON_COLOR, fg=FG_COLOR, font=("Arial", 12),
              command=lambda p=rel_path: run_script(p)).pack(pady=4, padx=10)

status_label = tk.Label(root, text="Ready", font=("Arial", 12),
                        bg=BG_COLOR, fg=SUCCESS_COLOR)
status_label.pack(pady=5)

tk.Label(root, text="Output", font=("Arial", 14, "bold"),
         bg=BG_COLOR, fg=FG_COLOR).pack(pady=5)

output_text = tk.Text(root, height=10, width=90, wrap="word",
                      bg="#1e1e1e", fg=FG_COLOR, insertbackground=FG_COLOR)
output_text.pack(pady=10)

tk.Button(root, text="Exit", width=20, font=("Arial", 12),
          bg=BUTTON_COLOR, fg=FG_COLOR, command=root.quit).pack(pady=10)

root.mainloop()
