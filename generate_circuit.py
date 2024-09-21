# We'll generate a DOT file format for Graphviz visualization of the circuit.
# Parsing the provided AIGER circuit information and creating the corresponding graph structure.

from graphviz import Digraph

# Initialize a directed graph
dot = Digraph(comment='AIGER Circuit')

# Define inputs, latches, and outputs
inputs = {
    'i0': 'charging_complete',
    'i1': 'call_from_0',
    'i2': 'call_from_1',
    'i3': 'call_from_2',
    'i4': 'call_from_3'
}

latches = {
    'l0': 'l0',
    'l1': 'l1',
    'l2': 'l2'
}

outputs = {
    'o0': 'deliver_power',
    'o1': 'service_location_0',
    'o2': 'service_location_1',
    'o3': 'service_location_2',
    'o4': 'service_location_3'
}

# AND gates represented as (output, input1, input2)
and_gates = [
    (18, 13, 15),
    (20, 17, 18),
    (22, 3, 21),
    (24, 3, 14),
    (26, 17, 24),
    (28, 21, 27),
    (30, 12, 24),
    (32, 16, 31),
    (34, 28, 33),
    (36, 12, 14),
    (38, 2, 37),
    (40, 16, 39),
    (42, 2, 40),
    (44, 13, 26),
    (46, 16, 18),
    (48, 45, 47),
    (50, 16, 19),
    (52, 37, 50),
    (54, 17, 30),
    (56, 53, 55),
    (58, 25, 40),
    (60, 23, 35),
    (62, 28, 53)
]

# Add input nodes
for i, label in inputs.items():
    dot.node(i, label, shape='ellipse')

# Add latch nodes
for l, label in latches.items():
    dot.node(l, label, shape='box')

# Add output nodes
for o, label in outputs.items():
    dot.node(o, label, shape='ellipse')

# Add AND gate nodes
for (output, input1, input2) in and_gates:
    gate_label = f'AND_{output}'
    dot.node(str(output), gate_label, shape='circle')
    dot.edge(str(input1), str(output))
    dot.edge(str(input2), str(output))

# Generate the graph
dot_data = dot.source
dot_data


print(dot_data)

# Render the graph
dot.render('circuit.png', view=True, format='png')