import tkinter as tk
from tkinter import messagebox

def check_password():
    password = entry_password.get()
    if len(password) < 8:
        result_label.config(text="Weak: Password is too short!", fg="#FF6B6B")
    elif password.isnumeric() or password.isalpha():
        result_label.config(text="Weak: Add letters and numbers!", fg="#FFA36C")
    else:
        result_label.config(text="Strong password!", fg="#4CAF50")

# Create main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.configure(bg="#F4F4F4")

# Header Frame
header_frame = tk.Frame(root, bg="#007ACC", height=60)
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="Password Strength Checker", 
                        font=("Arial", 16, "bold"), bg="#007ACC", fg="white")
header_label.pack(pady=15)

# Content Frame
content_frame = tk.Frame(root, bg="#F4F4F4", padx=20, pady=20)
content_frame.pack(fill="both", expand=True)

# Input Label
input_label = tk.Label(content_frame, text="Enter your password:", 
                       font=("Arial", 12), bg="#F4F4F4", fg="#333")
input_label.grid(row=0, column=0, pady=10, sticky="w")

# Entry Box with password masking
entry_password = tk.Entry(content_frame, font=("Arial", 12), width=30, 
                          relief="solid", highlightbackground="#CCC", highlightthickness=1, show="*")
entry_password.grid(row=1, column=0, pady=10, sticky="w")

# Check Button
btn_check = tk.Button(content_frame, text="Check Strength", font=("Arial", 12, "bold"), 
                       bg="#007ACC", fg="white", relief="flat", padx=10, pady=5, 
                       activebackground="#005F9E", activeforeground="white", command=check_password)
btn_check.grid(row=2, column=0, pady=20, sticky="w")

# Output Label
result_label = tk.Label(content_frame, text="",
                        font=("Arial", 12), bg="#F4F4F4", fg="#333")
result_label.grid(row=3, column=0, pady=10, sticky="w")

# Status Bar
status_bar = tk.Frame(root, bg="#E0E0E0", height=30)
status_bar.pack(fill="x")
status_label = tk.Label(status_bar, text="© 2024 MyApp by Samuel-Noah Osarenkhoe | All Rights Reserved", 
                        font=("Arial", 10), bg="#E0E0E0", fg="#777")
status_label.pack()

# Run the application
root.mainloop()
