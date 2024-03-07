import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes (representing sets A and B)
G.add_node("A", pos=(0, 1))
G.add_node("B", pos=(1, 1))
G.add_node("L", pos=(0.5, 0))  # L represents the colimit

# Add edges (representing the function f and the morphisms to L)
G.add_edge("A", "B", label='f')
G.add_edge("A", "L", label='')
G.add_edge("B", "L", label='')

# Draw the graph
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=15, font_weight='bold')
labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Colimit Visualization in a Simple Diagram")
plt.show()

