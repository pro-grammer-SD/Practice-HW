import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Length Converter App")

label = tk.Label(root, text="Enter length in meters:", font=("Arial", 12), fg="#333", bg="#e0f7fa")
label.pack(pady=10)

entry = tk.Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="#00695c")
result_label.pack(pady=10)

def convert():
    try:
        meters = float(entry.get())
        feet = meters * 3.28084
        result_label.config(text=f"{meters} meters = {feet:.2f} feet")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

button = tk.Button(root, text="Convert to Feet", command=convert, font=("Arial", 12), bg="#80cbc4")
button.pack(pady=10)

root.mainloop()
