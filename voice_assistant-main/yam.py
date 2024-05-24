import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.create_widgets()

    def create_widgets(self):
        # Create input fields and labels for password length and character types
        tk.Label(self.root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        self.length_var = tk.IntVar(value=12)
        tk.Entry(self.root, textvariable=self.length_var).grid(row=0, column=1, padx=10, pady=10)

        self.letters_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Letters", variable=self.letters_var).grid(row=1, column=0, columnspan=2)
        
        self.digits_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var).grid(row=2, column=0, columnspan=2)
        
        self.symbols_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, text="Include Symbols", variable=self.symbols_var).grid(row=3, column=0, columnspan=2)

        # Create a button to generate the password
        tk.Button(self.root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=10)

        # Create a field to display the generated password
        self.password_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.password_var, state='readonly').grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Create a button to copy the password to the clipboard
        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        use_letters = self.letters_var.get()
        use_digits = self.digits_var.get()
        use_symbols = self.symbols_var.get()

        if not (use_letters or use_digits or use_symbols):
            messagebox.showwarning("Input Error", "You must select at least one type of character (letters, digits, or symbols).")
            return

        char_set = ""
        if use_letters:
            char_set += string.ascii_letters
        if use_digits:
            char_set += string.digits
        if use_symbols:
            char_set += string.punctuation

        password = ''.join(random.choice(char_set) for _ in range(length))
        self.password_var.set(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
