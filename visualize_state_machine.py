from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Vehicle State Machine')

# Define states as nodes
states = ['OFF', 'BOOTING', 'IDLE', 'DRIVING', 'ERROR']
for state in states:
    if state == 'ERROR':
        dot.node(state, state, color='red')
    else:
        dot.node(state, state)

# Define transitions
transitions = {
    'OFF': {'power_on': 'BOOTING'},
    'BOOTING': {'boot_complete': 'IDLE', 'fault': 'ERROR'},
    'IDLE': {'start_drive': 'DRIVING', 'fault': 'ERROR'},
    'DRIVING': {'stop_drive': 'IDLE', 'fault': 'ERROR'},
    'ERROR': {'reset': 'OFF'},
}

# Add edges for transitions
for from_state, events in transitions.items():
    for event, to_state in events.items():
        dot.edge(from_state, to_state, label=event)

# Save and render the diagram
print("DOT source for the state machine diagram:")
print(dot.source)
# dot.render('vehicle_state_machine', format='png', view=True)
print("State machine diagram DOT source generated above. You can copy this to an online Graphviz viewer.")