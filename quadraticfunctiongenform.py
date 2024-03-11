import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_quadratic():
    a = a_slider.get()
    b = b_slider.get()
    c = c_slider.get()

    # Update the equations
    general_form.config(text=f"General Form: y = {a:.2f}x² + {b:.2f}x + {c:.2f}")
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)
    canonical_form.config(text=f"Canonical Form: y = {a:.2f}(x - {h:.2f})² + {k:.2f}")

    # Plotting
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    ax.clear()
    ax.plot(x, y)
    ax.set_title("Quadratic Function")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_ylim(-10, 10)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    canvas.draw()

app = tk.Tk()
app.title("Quadratic Function Visualizer")

# Create labels and sliders for a, b, c
tk.Label(app, text="a: ").pack()
a_slider = ttk.Scale(app, from_=-2.0, to=2.0, orient='horizontal')
a_slider.set(1)
a_slider.pack()

tk.Label(app, text="b: ").pack()
b_slider = ttk.Scale(app, from_=-5, to=5, orient='horizontal')
b_slider.set(0)
b_slider.pack()

tk.Label(app, text="c: ").pack()
c_slider = ttk.Scale(app, from_=-10, to=10, orient='horizontal')
c_slider.set(0)
c_slider.pack()

# Set commands for sliders after they are defined
a_slider.config(command=lambda s: plot_quadratic())
b_slider.config(command=lambda s: plot_quadratic())
c_slider.config(command=lambda s: plot_quadratic())

# Equation labels
general_form = tk.Label(app, text="")
general_form.pack()
canonical_form = tk.Label(app, text="")
canonical_form.pack()

# Create the plot
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=app)
widget = canvas.get_tk_widget()
widget.pack()

plot_quadratic()

app.mainloop()

