import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def update_formulas(a, b, c):
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)

    general_formula_ax.clear()
    general_formula_ax.text(0.5, 0.5, f"$y = {a:.2f}x^2 + {b:.2f}x + {c:.2f}$", 
                            fontsize=12, ha='center', va='center')
    general_formula_ax.axis('off')

    canonical_formula_ax.clear()
    canonical_formula_ax.text(0.5, 0.5, f"$y = {a:.2f}(x - {h:.2f})^2 + {k:.2f}$", 
                              fontsize=12, ha='center', va='center')
    canonical_formula_ax.axis('off')

    formula_canvas.draw()

def plot_quadratic():
    a = a_slider.get()
    b = b_slider.get()
    c = c_slider.get()

    update_formulas(a, b, c)

    # Plotting
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    ax.clear()
    ax.plot(x, y, label="Quadratic Function")

    # Plot vertex path
    b_values = np.linspace(-5, 5, 100)
    h_values = -b_values / (2 * a)
    k_values = c - (b_values ** 2) / (4 * a)
    ax.plot(h_values, k_values, 'r--', label="Vertex Path")

    # Highlight current vertex
    ax.plot(-b / (2 * a), c - (b ** 2) / (4 * a), 'ro')

    ax.set_title("Quadratic Function and Vertex Path")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_ylim(-10, 10)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()
    canvas.draw()

app = tk.Tk()
app.title("Quadratic Function Visualizer")

# Create labels and sliders for a, b, c
tk.Label(app, text="a (constant): ").pack()
a_slider = ttk.Scale(app, from_=-2.0, to=2.0, orient='horizontal')
a_slider.set(1)  # Set a constant value for a
a_slider.pack()

tk.Label(app, text="b: ").pack()
b_slider = ttk.Scale(app, from_=-5, to=5, orient='horizontal')
b_slider.set(0)
b_slider.pack()

tk.Label(app, text="c (constant): ").pack()
c_slider = ttk.Scale(app, from_=-10, to=10, orient='horizontal')
c_slider.set(0)  # Set a constant value for c
c_slider.pack()

# Set commands for sliders after they are defined
a_slider.config(command=lambda s: plot_quadratic())
b_slider.config(command=lambda s: plot_quadratic())
c_slider.config(command=lambda s: plot_quadratic())

# Create the plot for the function
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=app)
widget = canvas.get_tk_widget()
widget.pack()

# Create the plot for the formulas
formula_fig = Figure(figsize=(10, 2))  # Adjusted figure size
general_formula_ax = formula_fig.add_subplot(121)
canonical_formula_ax = formula_fig.add_subplot(122)
formula_canvas = FigureCanvasTkAgg(formula_fig, master=app)
formula_widget = formula_canvas.get_tk_widget()
formula_widget.pack()

plot_quadratic()

app.mainloop()

