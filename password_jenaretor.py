# password_gui.py
import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

try:
    import pyperclip
    HAVE_PYPERCLIP = True
except Exception:
    HAVE_PYPERCLIP = False

def generate_password(length=12, use_upper=True, use_digits=True, use_punct=True):
    chars = list(string.ascii_lowercase)
    if use_upper:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_punct:
        chars += list("!@#$%^&*()-_=+[]{};:,.<>?")
    if not chars:
        return ""
    return "".join(random.choice(chars) for _ in range(length))

def on_generate():
    length = length_var.get()
    up = upper_var.get()
    dg = digit_var.get()
    pu = punct_var.get()
    pwd = generate_password(length, up, dg, pu)
    result_var.set(pwd)

def on_copy():
    pwd = result_var.get()
    if not pwd:
        messagebox.showinfo("No password", "প্রথমে পাসওয়ার্ড জেনারেট করুন।")
        return
    if HAVE_PYPERCLIP:
        pyperclip.copy(pwd)
    else:
        root.clipboard_clear()
        root.clipboard_append(pwd)
    messagebox.showinfo("Copied", "পাসওয়ার্ড clipboard-এ কপি করা হয়েছে।")

root = tk.Tk()
root.title("Password Generator")
root.geometry("420x220")
root.resizable(False, False)

frame = ttk.Frame(root, padding=12)
frame.pack(fill="both", expand=True)

length_var = tk.IntVar(value=12)
upper_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
punct_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
length_scale = ttk.Scale(frame, from_=6, to=32, orient="horizontal", command=lambda e: length_var.set(int(float(e))))
length_scale.set(12)
length_scale.grid(row=0, column=1, sticky="we", padx=8)
ttk.Label(frame, textvariable=length_var).grid(row=0, column=2, sticky="e")

ttk.Checkbutton(frame, text="Include Uppercase", variable=upper_var).grid(row=1, column=0, columnspan=3, sticky="w")
ttk.Checkbutton(frame, text="Include Digits", variable=digit_var).grid(row=2, column=0, columnspan=3, sticky="w")
ttk.Checkbutton(frame, text="Include Symbols", variable=punct_var).grid(row=3, column=0, columnspan=3, sticky="w")

ttk.Button(frame, text="Generate", command=on_generate).grid(row=4, column=0, pady=12)
ttk.Entry(frame, textvariable=result_var, width=30).grid(row=4, column=1, columnspan=1, sticky="we")
ttk.Button(frame, text="Copy", command=on_copy).grid(row=4, column=2)

for i in range(3):
    frame.columnconfigure(i, weight=1)

root.mainloop()
print("your name")
