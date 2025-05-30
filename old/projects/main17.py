import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        name = name_entry.get().strip()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birthdate = datetime(year, month, day)
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        result_label.config(text=f"Hey {name}, you are {age} years old!")
    except ValueError:
        result_label.config(text="Invalid input. Try again.")

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=40)

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame, text="Day:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame, text="Month:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame, text="Year:").grid(row=3, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(frame, width=20)
day_entry = tk.Entry(frame, width=20)
month_entry = tk.Entry(frame, width=20)
year_entry = tk.Entry(frame, width=20)

name_entry.grid(row=0, column=1, pady=5)
day_entry.grid(row=1, column=1, pady=5)
month_entry.grid(row=2, column=1, pady=5)
year_entry.grid(row=3, column=1, pady=5)

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
