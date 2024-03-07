#Combinatorics Visualizer
#Overview:
#This interactive Python application is designed to aid in the understanding of fundamental combinatorics concepts, focusing particularly on combinations. It allows users to explore how different combinations can be formed from a set of elements. The application visually represents the combinatorial concepts using a combination tree, enhancing the learning experience through interactive and graphical elements.
#
#Features:
#
#User Input for Combinatorial Parameters:
#
#Users can input two main parameters: the total number of elements (n) and the number of elements to choose (r).
#The application then calculates the number of possible combinations (nCr).
#Combination Calculation:
#
#Utilizing the standard combination formula (nCr = n! / [r! × (n-r)!]), the application computes the total number of unique combinations possible.
#This calculation is dynamically updated based on user inputs.
#Graphical Combination Tree:
#
#The core feature of the application is its ability to generate and display a combination tree.
#Each node of the tree represents a unique combination, providing a clear visual representation of how each combination is formed.
#Interactive Tree Visualization:
#
#The tree is structured using networkx and matplotlib to create a multipartite layout, where each level of the tree corresponds to the size of the combinations.
#Users can see how the tree evolves as they change the parameters (n and r), offering an intuitive grasp of the combinatorial process.
#User-Friendly Interface:
#
#Built with Tkinter, the application presents a simple and intuitive interface, suitable for educational purposes.
#Inputs, calculations, and visualizations are presented in a clear and concise manner, making it accessible for learners at different levels.
#Educational Benefits:
#
#Conceptual Understanding: By interacting with the visual elements and seeing immediate responses to input changes, users can develop a deeper understanding of combinatorial concepts.
#Intuitive Learning: The application demystifies complex combinatorial calculations, presenting them in an easy-to-understand visual format.
#Engagement and Interactivity: The hands-on approach fosters engagement, encouraging learners to explore and experiment with different scenarios.
#Usage Scenarios:
#
#Educational Settings: Ideal for classrooms or individual learning, particularly in courses covering basic mathematics, probability, or computer science.
#Self-Learning: Useful for students or individuals looking to self-study or reinforce their understanding of combinatorics.
#Problem Solving: Assists in visualizing and solving combinatorial problems, especially those involving combinations.
#

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
