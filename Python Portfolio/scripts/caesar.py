import tkinter as tk

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    result_label.config(text=f"Here is the {encode_or_decode}d result:\n{output_text}")


def run_cipher():
    direction = direction_var.get()
    text = text_input.get("1.0", tk.END).strip().lower()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number for shift.")
        return

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)


# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher")

# Logo (optional)
logo_label = tk.Label(root, text=logo, font=("Courier", 8), justify="left")
logo_label.pack()

# Dropdown for direction
direction_var = tk.StringVar(value="encode")
direction_frame = tk.Frame(root)
direction_frame.pack(pady=5)
tk.Label(direction_frame, text="Choose action: ").pack(side="left")
tk.OptionMenu(direction_frame, direction_var, "encode", "decode").pack(side="left")

# Message input
text_label = tk.Label(root, text="Type your message:")
text_label.pack()
text_input = tk.Text(root, height=4, width=50)
text_input.pack(pady=5)

# Shift input
shift_label = tk.Label(root, text="Type the shift number:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack(pady=5)

# Run button
run_button = tk.Button(root, text="Run Caesar Cipher", command=run_cipher)
run_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Courier", 10), justify="left", wraplength=400)
result_label.pack(pady=10)

root.mainloop()
