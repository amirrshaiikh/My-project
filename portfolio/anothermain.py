import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import threading
import sys

if getattr(sys, 'frozen', False):
    # Running as compiled with PyInstaller
    base_dir = sys._MEIPASS
else:
    # Running as a normal Python script
    base_dir = os.path.dirname(os.path.abspath(__file__))
# ====== SETTINGS ======

SCRIPTS = {
    "Tip Calculator": "/scripts/D2TipCalculator.py",
    "Pizza Maker": os.path.join(base_dir, "scripts", "D3Pizza.py"),
    "Treasure Island": os.path.join(base_dir, "scripts", "D3TreasureIsland.py"),
    "Rock, Paper, Scissor": os.path.join(base_dir, "scripts", "D4RockPaper.py"),
    "Password Generator": os.path.join(base_dir, "scripts", "D5PasswordGenerator.py"),
    "Hangman Game": os.path.join(base_dir, "scripts", "Hangman", "Day7- Hangman.py"),
    "Cipher Code": os.path.join(base_dir, "scripts", "D8CaesarCipher.py"),
    "Calculator": os.path.join(base_dir, "scripts", "D10Calc.py"),
    "BlackJack": os.path.join(base_dir, "scripts", "D11Blackjack.py"),
    "Guess the Number": os.path.join(base_dir, "scripts", "D12NumberGuessing.py"),
    "Higher Lower Game": os.path.join(base_dir, "scripts", "HigherLower", "main.py"),
    "Coffe Vending Machine": os.path.join(base_dir, "scripts", "CoffeeMachine", "main.py"),
    "Random Walk": os.path.join(base_dir, "scripts", "D18RandomWalk.py"),
    "Spirograph": os.path.join(base_dir, "scripts", "D18Spirograph.py"),
    "Hirst Painting": os.path.join(base_dir, "scripts", "D18Hirst.py"),
    "Etch a Sketch": os.path.join(base_dir, "scripts", "D19EtchASketch.py"),
    "Turtle Race": os.path.join(base_dir, "scripts", "D19Race.py"),
    "Snake Game": os.path.join(base_dir, "scripts", "Snake", "main.py"),
    "Pong Game": os.path.join(base_dir, "scripts", "Pong", "main.py"),
    "Turtle Crossing": os.path.join(base_dir, "scripts", "TurtleCrossing", "main.py"),
    "Guess the US states": os.path.join(base_dir, "scripts", "USStatesGuess", "main.py"),
    "Pounds to Kg Converter": os.path.join(base_dir, "scripts", "D27PoundstoKg.py")
}



BG_COLOR = "#2b2b2b"       # Dark background
FG_COLOR = "#ffffff"       # White text
BUTTON_COLOR = "#444444"
HIGHLIGHT_COLOR = "#00bfff"
SUCCESS_COLOR = "#32CD32"
ERROR_COLOR = "#ff4c4c"

# ====== FUNCTIONS ======

def run_script(script_path):
    output_text.delete(1.0, tk.END)
    status_label.config(text="Running...", fg=HIGHLIGHT_COLOR)

    def execute():
        try:
            if not os.path.exists(script_path):
                raise FileNotFoundError(f"Script not found: {script_path}")

            # Use sys.executable for dynamic Python path (in case of venvs)
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
                output_text.insert(tk.END, "\nERROR:\n" + stderr)
                status_label.config(text="Error occurred", fg=ERROR_COLOR)
            else:
                status_label.config(text="Done", fg=SUCCESS_COLOR)

        except FileNotFoundError as fnf_error:
            messagebox.showerror("File Not Found", str(fnf_error))
            status_label.config(text="Script not found", fg=ERROR_COLOR)

        except Exception as e:
            output_text.insert(tk.END, f"\nUnexpected Error:\n{str(e)}")
            status_label.config(text="Error", fg=ERROR_COLOR)

    threading.Thread(target=execute, daemon=True).start()

# ====== MAIN WINDOW ======
root = tk.Tk()
root.title("My Python Portfolio")
root.geometry("800x600")
root.config(bg=BG_COLOR)

# ====== TITLE ======
title_label = tk.Label(root, text="My Python Projects", font=("Arial", 18, "bold"),
                       bg=BG_COLOR, fg=HIGHLIGHT_COLOR)
title_label.pack(pady=10)

# ====== SCROLLABLE FRAME FOR BUTTONS ======
frame_container = tk.Frame(root, bg=BG_COLOR)
frame_container.pack(pady=10, fill="both", expand=True)

canvas = tk.Canvas(frame_container, bg=BG_COLOR, highlightthickness=0)
scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Enable scrolling via mouse wheel
def _on_mouse_wheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# ====== ADD SCRIPT BUTTONS ======
for name, path in SCRIPTS.items():
    btn = tk.Button(scrollable_frame, text=name, width=40, anchor="w",
                    bg=BUTTON_COLOR, fg=FG_COLOR, font=("Arial", 12),
                    command=lambda p=path: run_script(p))
    btn.pack(pady=4, padx=10)

# ====== STATUS LABEL ======
status_label = tk.Label(root, text="Ready", font=("Arial", 12),
                        bg=BG_COLOR, fg=SUCCESS_COLOR)
status_label.pack(pady=5)

# ====== OUTPUT LABEL ======
output_label = tk.Label(root, text="Output", font=("Arial", 14, "bold"),
                        bg=BG_COLOR, fg=FG_COLOR)
output_label.pack(pady=5)

# ====== OUTPUT TEXT BOX ======
output_text = tk.Text(root, height=10, width=90, wrap="word",
                      bg="#1e1e1e", fg=FG_COLOR, insertbackground=FG_COLOR)
output_text.pack(pady=10)

# ====== EXIT BUTTON ======
exit_btn = tk.Button(root, text="Exit", width=20, font=("Arial", 12),
                     bg=BUTTON_COLOR, fg=FG_COLOR, command=root.quit)
exit_btn.pack(pady=10)

# ====== RUN THE APP ======
root.mainloop()                                                                          