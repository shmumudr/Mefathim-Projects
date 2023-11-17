import tkinter as tk
from tkinter import messagebox

# Define the validation function
def validate_id():
    user_id = user_id_entry.get()

    if len(user_id) != 9 or not user_id.isdigit():
        messagebox.showerror("Error", "Please enter a valid 9-digit ID.")
        return

    if valid_id(user_id):
        messagebox.showinfo("Success", "Valid ID!")
    else:
        messagebox.showerror("Error", "Invalid ID!")

# Define the ID validation function (your existing code)
def valid_id(user_id):
    user_id = list(user_id)

    first_8_digits = user_id[:8]
    total_sum = 0
    index = 1

    for i in first_8_digits:
        if index % 2 != 0:
            i = int(i)
            total_sum += i
            index += 1
        else:
            i = int(i) * 2
            i = (i // 10) + (i % 10) if i > 10 else i
            total_sum += i
            index += 1

    next_number = (10 - total_sum % 10) % 10

    return next_number == int(user_id[8])

# Create the main window
window = tk.Tk()
window.title("ID Validation")

# Create and place widgets
user_id_label = tk.Label(window, text="Enter a 9-digit ID:")
user_id_label.pack(pady=100)

user_id_entry = tk.Entry(window)
user_id_entry.pack()

validate_button = tk.Button(window, text="Validate ID", command=validate_id)
validate_button.pack(pady=10)

# Start the GUI main loop
window.mainloop()
