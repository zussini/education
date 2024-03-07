import tkinter as tk
from math import factorial

def calculate_combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def update_tree():
    n = int(entry_n.get())
    r = int(entry_r.get())
    num_combinations = calculate_combinations(n, r)
    label_result.config(text=f"Number of combinations: {num_combinations}")
    # Here you would add the logic to update the combination tree visualization

# Set up the basic window
window = tk.Tk()
window.title("Combinatorics Learning Tool")

# Create input fields for n and r
label_n = tk.Label(window, text="Total number of balls (n):")
label_n.pack()
entry_n = tk.Entry(window)
entry_n.pack()

label_r = tk.Label(window, text="Number of balls to draw (r):")
label_r.pack()
entry_r = tk.Entry(window)
entry_r.pack()

# Button to calculate combinations
button_calculate = tk.Button(window, text="Calculate Combinations", command=update_tree)
button_calculate.pack()

# Label to display results
label_result = tk.Label(window, text="")
label_result.pack()

# Start the GUI event loop
window.mainloop()

