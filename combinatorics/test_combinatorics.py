import tkinter as tk
from math import factorial
import networkx  as nx
import  matplotlib.pyplot  as plt
from itertools import combinations

def calculate_combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))




def draw_combination_tree(n, r):
    G = nx.Graph()
    
    # Add nodes with a subset attribute for each combination
    for subset_size in range(r + 1):
        for combo in combinations(range(n), subset_size):
            G.add_node(str(combo), subset=subset_size)

    # Add edges between nodes
    for node in G.nodes:
        node_set = eval(node)
        for i in range(n):
            if i not in node_set:
                next_node = str(tuple(sorted(list(node_set) + [i])))
                if next_node in G.nodes:
                    G.add_edge(node, next_node)

    # Draw the graph using a multipartite layout
    pos = nx.multipartite_layout(G, subset_key="subset")  # Use the 'subset' attribute
    nx.draw(G, pos, with_labels=True)
    plt.show()


def update_tree():
    n = int(entry_n.get())
    r = int(entry_r.get())
    num_combinations = calculate_combinations(n, r)
    label_result.config(text=f"Number of combinations: {num_combinations}")

    # Draw the combination tree directly
    draw_combination_tree(n, r)

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

# Button to calculate combinations and draw the tree
button_calculate = tk.Button(window, text="Calculate and Draw Tree", command=update_tree)
button_calculate.pack()

# Label to display results
label_result = tk.Label(window, text="")
label_result.pack()

# Start the GUI event loop
window.mainloop()

