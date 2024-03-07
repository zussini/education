import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes for each category of reasoning development
G.add_nodes_from(["Mom", "Non-Mom", "Family", "Friends", "Emotions", "Ethics"])

# Add edges representing the development of reasoning
G.add_edges_from([("Mom", "Family"), ("Non-Mom", "Friends"), 
                  ("Family", "Emotions"), ("Friends", "Emotions"),
                  ("Emotions", "Ethics")])

# Draw the graph
nx.draw(G, with_labels=True, node_color='lightblue', font_size=10, font_weight='bold')
plt.show()

