import re
from graphviz import Digraph
from generate_aiger import files


def parse_aiger_file(file_content):
    # Parse the header
    lines = file_content.strip().split('\n')
    header = lines[1].split()  # Example: ['aag', '31', '5', '3', '5', '23']
    
    inputs = []
    latches = []
    outputs = []
    and_gates = []

    num_inputs = int(header[1])
    num_latches = int(header[2])
    num_outputs = int(header[3])
    num_and_gates = int(header[4])

    # Extract the sections of inputs, latches, outputs, and AND gates
    i = 2
    current_section = 'inputs'
    
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('i'):
            inputs.append(line)
        elif line.startswith('l'):
            latches.append(line)
        elif line.startswith('o'):
            outputs.append(line)
        elif re.match(r'^\d+', line):
            and_gates.append(line)
        i += 1

    return inputs, latches, outputs, and_gates

def render_aiger_graph(inputs, latches, outputs, and_gates):
    # Initialize the graph
    dot = Digraph(comment='AIGER Circuit')

    # Add inputs
    for input_signal in inputs:
        input_id, signal_name = input_signal.split()
        dot.node(input_id, label=signal_name, shape='ellipse')

    # Add latches
    for latch in latches:
        latch_id, signal_name = latch.split()
        dot.node(latch_id, label=signal_name, shape='box')

    # Add outputs
    for output in outputs:
        output_id, signal_name = output.split()
        dot.node(output_id, label=signal_name, shape='doublecircle')

    # Add AND gates
    for and_gate in and_gates:
        components = and_gate.split()

        if len(components) == 1:
            # Gate has only an ID, no inputs
            and_id = components[0]
            dot.node(and_id, label=f'AND {and_id}', shape='diamond')
        elif len(components) == 3:
            # Gate has ID and two inputs
            and_id, input1, input2 = components
            dot.node(and_id, label=f'AND {and_id}', shape='diamond')
            dot.edge(input1, and_id)
            dot.edge(input2, and_id)
        else:
            # Unexpected format, you can log or handle the case
            print(f"Unexpected AND gate format: {components}")

    return dot

for filename in files:
    # Try to open file and read it
    try:
        open("data/" + filename + ".aiger")
    except FileNotFoundError:
        print(f"File not found: {filename}")
        continue
    # Parse the AIGER file content
    file_content = open("data/" + filename + ".aiger").read()
    # If the file is empty, skip it
    if not file_content:
        print(f"File is empty: {filename}")
        continue
    inputs, latches, outputs, and_gates = parse_aiger_file(file_content)

    # Render the graph
    dot = render_aiger_graph(inputs, latches, outputs, and_gates)

    # Save the graph to a file and render it
    dot.render("data/" + filename, format='png')

    print(f"Graph saved to: {filename}.png")
