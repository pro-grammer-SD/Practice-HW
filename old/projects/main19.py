import tkinter as tk
from tkinter import ttk

def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())
        
        si = (p * t * r) / 100
        ci = p * ((1 + r / 100) ** t) - p
        
        si_result.config(text=f"Simple Interest: ₹{si:.2f}")
        ci_result.config(text=f"Compound Interest: ₹{ci:.2f}")
    except ValueError:
        si_result.config(text="Enter valid numbers.")
        ci_result.config(text="")

root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")
root.configure(bg="#f0f4c3")

frame = ttk.Frame(root)
frame.place(relx=0.5, rely=0.3, anchor="center")

tk.Label(frame, text="Principal:", font=("Arial", 11), bg="#f0f4c3").grid(row=0, column=0, padx=10, pady=5, sticky="e")
principal_entry = tk.Entry(frame, width=20, font=("Arial", 11))
principal_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Time (years):", font=("Arial", 11), bg="#f0f4c3").grid(row=1, column=0, padx=10, pady=5, sticky="e")
time_entry = tk.Entry(frame, width=20, font=("Arial", 11))
time_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Rate (%):", font=("Arial", 11), bg="#f0f4c3").grid(row=2, column=0, padx=10, pady=5, sticky="e")
rate_entry = tk.Entry(frame, width=20, font=("Arial", 11))
rate_entry.grid(row=2, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Calculate", command=calculate_interest, font=("Arial", 12), bg="#aed581")
calc_button.place(relx=0.5, rely=0.5, anchor="center")

si_result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f4c3", fg="#33691e")
si_result.place(relx=0.5, rely=0.6, anchor="center")

ci_result = tk.Label(root, text="", font=("Arial", 12), bg="#f0f4c3", fg="#33691e")
ci_result.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
