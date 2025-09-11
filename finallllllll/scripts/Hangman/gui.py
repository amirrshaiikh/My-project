import tkinter as tk
import random
import hangman_words, hangman_art

# ------------------- GAME LOGIC ------------------- #
class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("800x700")
        self.root.configure(bg="black")

        self.lives = 6
        self.chosen_word = random.choice(hangman_words.word_list)
        self.correct_letters = []
        self.display = "_" * len(self.chosen_word)

        # ------------------- UI ------------------- #
        self.logo_label = tk.Label(root, text=hangman_art.logo, font=("Courier", 10),
                                   fg="lime", bg="black", justify="left")
        self.logo_label.pack(pady=10)

        self.word_label = tk.Label(root, text="Word to guess: " + self.display,
                                   font=("Arial", 20), fg="white", bg="black")
        self.word_label.pack(pady=20)

        self.lives_label = tk.Label(root, text=f"Lives: {self.lives}/6",
                                    font=("Arial", 16), fg="red", bg="black")
        self.lives_label.pack()

        self.hangman_label = tk.Label(root, text=hangman_art.stages[self.lives],
                                      font=("Courier", 12), fg="yellow", bg="black", justify="left")
        self.hangman_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 16), width=5, justify="center")
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", command=self.make_guess,
                                      font=("Arial", 14), bg="green", fg="white")
        self.guess_button.pack(pady=5)

        self.message_label = tk.Label(root, text="", font=("Arial", 14), fg="cyan", bg="black")
        self.message_label.pack(pady=10)

    # ------------------- GAME FUNCTION ------------------- #
    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess or len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter!")
            return

        if guess in self.correct_letters:
            self.message_label.config(text=f"You already guessed '{guess}'")
            return

        display_list = list(self.display)

        if guess in self.chosen_word:
            for idx, letter in enumerate(self.chosen_word):
                if letter == guess:
                    display_list[idx] = guess
            self.display = "".join(display_list)
            self.correct_letters.append(guess)
            self.word_label.config(text="Word to guess: " + self.display)
            self.message_label.config(text=f"Good job! '{guess}' is correct!")
        else:
            self.lives -= 1
            self.message_label.config(text=f"'{guess}' is not in the word. You lost a life!")
            self.hangman_label.config(text=hangman_art.stages[self.lives])
            self.lives_label.config(text=f"Lives: {self.lives}/6")

        # Check Win
        if "_" not in self.display:
            self.message_label.config(text="🎉 YOU WIN! 🎉")
            self.guess_button.config(state="disabled")

        # Check Lose
        if self.lives == 0:
            self.word_label.config(text=f"The word was: {self.chosen_word}")
            self.message_label.config(text="💀 YOU LOSE 💀")
            self.guess_button.config(state="disabled")


# ------------------- RUN APP ------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
