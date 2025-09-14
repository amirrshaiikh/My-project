import tkinter as tk
import subprocess
import os
import sys

# Path setup
base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Your scripts list (shortened for demo)
SCRIPTS = {
    # "Tip Calculator": "scripts/D2TipCalculator.py",
    # "Pizza Maker": "scripts/D3Pizza.py",
    # "Treasure Island": "scripts/D3TreasureIsland.py",
    # "Rock, Paper, Scissor": "scripts/D4RockPaper.py",
    # "Password Generator": "scripts/D5PasswordGenerator.py",
    "Hangman Game": "scripts/Hangman/gui.py",
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

def run_script(relative_path):
    script_path = os.path.join(base_dir, relative_path)
    output_box.delete("1.0", tk.END)
    status_label.config(text="Running...")

    try:
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"Script not found:\n{script_path}")

        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(script_path)
        )

        if result.stdout:
            output_box.insert(tk.END, "Output:\n" + result.stdout)
        if result.stderr:
            output_box.insert(tk.END, "Error:\n" + result.stderr)
            status_label.config(text="Error")
        else:
            status_label.config(text="Done")

    except Exception as e:
        output_box.insert(tk.END, f"Exception:\n{str(e)}")
        status_label.config(text="Failed")

# GUI Setup
root = tk.Tk()
root.title("My Python Projects")
root.geometry("600x500")

tk.Label(root, text="Select a Script to Run", font=("Arial", 14)).pack(pady=10)

# Script buttons
for name, path in SCRIPTS.items():
    tk.Button(root, text=name, width=30, command=lambda p=path: run_script(p)).pack(pady=4)

status_label = tk.Label(root, text="Ready", fg="green")
status_label.pack(pady=5)

tk.Label(root, text="Output:").pack()
output_box = tk.Text(root, height=10, width=70)
output_box.pack(pady=10)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
