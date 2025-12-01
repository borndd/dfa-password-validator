import tkinter as tk
from tkinter import messagebox


class DFAPasswordValidator:
    def __init__(self, min_length=6):
        self.min_length = min_length
        self.allowed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                           "abcdefghijklmnopqrstuvwxyz"
                           "0123456789")

    def validate(self, password):
        has_upper = False
        has_digit = False
        length_ok = False

        for i, ch in enumerate(password):

            if ch not in self.allowed:
                return False, f"Invalid character '{ch}' → DEAD STATE"

            if ch.isupper():
                has_upper = True
            if ch.isdigit():
                has_digit = True
            if i + 1 >= self.min_length:
                length_ok = True

 
        if has_upper and has_digit and length_ok:
            return True, "Password ACCEPTED (Reached accepting state)"
        else:
            if not length_ok:
                return False, "Rejected → Password must be at least 6 characters"
            if not has_upper:
                return False, "Rejected → Must contain at least one uppercase"
            if not has_digit:
                return False, "Rejected → Must contain at least one digit"



class PasswordValidatorGUI:
    def __init__(self, root):
        self.validator = DFAPasswordValidator()

        root.title("DFA Password Validator")
        root.geometry("400x250")
        root.resizable(False, False)


        self.title_label = tk.Label(
            root, text="Finite Automata Password Validator",
            font=("Arial", 14, "bold")
        )
        self.title_label.pack(pady=15)


        self.pass_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
        self.pass_label.pack()

        self.pass_entry = tk.Entry(root, show="", width=30, font=("Arial", 12))
        self.pass_entry.pack(pady=5)


        self.validate_btn = tk.Button(
            root, text="Validate",
            font=("Arial", 12),
            command=self.run_validation
        )
        self.validate_btn.pack(pady=15)

    def run_validation(self):
        password = self.pass_entry.get()
        valid, message = self.validator.validate(password)

        if valid:
            messagebox.showinfo("Result", message)
        else:
            messagebox.showerror("Result", message)



if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordValidatorGUI(root)
    root.mainloop()