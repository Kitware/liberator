"""
Does not quite work yet. Shows current limitations of liberator.
"""
import ubelt as ub
import networkx as nx

# Create a liberator object
import liberator
lib = liberator.Liberator(verbose=3)

# Add the code you want to use
lib.add_dynamic(nx.DiGraph)
lib.add_dynamic(nx.classes.coreviews.AdjacencyView)
lib.add_dynamic(nx.classes.reportviews.DegreeView)
lib.add_dynamic(nx.classes.reportviews.EdgeView)
lib.add_dynamic(nx.classes.reportviews.NodeView)
lib.add_dynamic(nx.exception.NetworkXError)
# lib.add_dynamic(nx.NetworkXError)  # Fix for failure mode? Nope.

# lib.expand(['networkx'])
lib.expand(['networkx.exception'])
lib.expand(['networkx.classes.coreviews'])
lib.expand(['networkx.classes.reportviews'])
lib.expand(['networkx.classes.graph'])
lib.expand(['networkx.convert'])

lib.expand(['networkx'])

# Extract the minimal code
source = lib.current_sourcecode()

demo_dpath = ub.Path.appdir('liberator/demo/nx').ensuredir()
demo_fpath = demo_dpath / 'nx_graph_standalone.py'
print(f'{demo_fpath}')

demo_fpath.write_text(source)
