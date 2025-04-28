import tkinter as tk

# Function to calculate the product
def calculate_product():
    try:
        # Get the values from the input fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        # Calculate the product
        product = num1 * num2
        
        # Display the result in the label
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Product Calculator")

# Create labels and input fields
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create a button to calculate the product
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="Product: ")
result_label.pack()

# Run the application
root.mainloop()
