import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x400")
app.title("Length Converter App")

def check_strength():
    pwd = entry.get()
    length = len(pwd)
    if length <= 5:
        result.configure(text="Weak", text_color="#FF0000")
    elif 6 <= length <= 8:
        result.configure(text="Medium", text_color="#FFD700")
    elif 9 <= length <= 12:
        result.configure(text="Strong", text_color="#90EE90")
    else:
        result.configure(text="Very Strong", text_color="#006400")

title = ctk.CTkLabel(app, text="Password Strength Checker", font=("Arial", 20))
title.pack(pady=20)

entry = ctk.CTkEntry(app, width=250, placeholder_text="Enter Password")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Check Strength", command=check_strength)
button.pack(pady=10)

result = ctk.CTkLabel(app, text="", font=("Arial", 18))
result.pack(pady=20)

app.mainloop()
