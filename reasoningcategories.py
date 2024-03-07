import networkx as nx
import matplotlib.pyplot as plt

# Creating a multi-level hierarchical graph
G = nx.DiGraph()

# Adding nodes for each cognitive process level
G.add_nodes_from(["Sensory Processing", "Basic Reasoning", "Higher-Order Reasoning"])
G.add_nodes_from(["State 1", "State 2", "State 3", "State 4"])  # Example states

# Adding edges representing regulatory mechanisms
G.add_edges_from([("Sensory Processing", "State 1"), ("Basic Reasoning", "State 2"),
                  ("Higher-Order Reasoning", "State 3"), ("State 2", "State 4")])

# Drawing the graph
nx.draw(G, with_labels=True)
plt.show()

