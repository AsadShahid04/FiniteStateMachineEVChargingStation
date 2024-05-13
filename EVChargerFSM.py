from transitions import Machine

# Define the state information
state_info = {
    'Idle': {
        'outputs': ['Connected'],
        'transitions': ['plug_in_vehicle']
    },
    'Connected': {
        'outputs': ['Idle', 'Charging'],
        'transitions': ['unplug_vehicle', 'ready_for_charging']
    },
    'Charging': {
        'outputs': ['Finished'],
        'transitions': ['charging_complete', 'pause_charging']
    },
    'Paused': {
        'outputs': ['Error'],
        'transitions': ['charging_error']
    },
    'Finished': {
        'outputs': ['Idle'],
        'transitions': ['unplug_vehicle_finished']
    },
    'Error': {
        'outputs': ['Maintenance'],
        'transitions': ['address_error']
    },
    'Maintenance': {
        'outputs': ["Idle"],
        'transitions': ['finish_maintenance']
    }
}

# Define the StateMachine
class EVCharger:
    pass

charging_station = Machine(model=EVCharger(), states=list(state_info.keys()), initial='Idle', send_event=True, queued=True)

# Add transitions and outputs to the state machine
for state, info in state_info.items():
    for transition, dest in zip(info['transitions'], info['outputs']):
        charging_station.add_transition(trigger=transition, source=state, dest=dest)

# Function to prompt user for input and transition to the next state
def prompt_for_transition():

    # Get the transitions for the 'Idle' state
    available_transitions = state_info[charging_station.model.state]['transitions']
    print("Transitions for " + charging_station.model.state +  " state are:", available_transitions)

    print("Current state:", charging_station.model.state)
    # available_transitions = charging_station.get_triggers()
    print("Available transitions:", available_transitions)
    selected_transition = input("Select a transition (type 'exit' to quit): ")
    if selected_transition == 'exit':
        return False
    if selected_transition in available_transitions:
        getattr(charging_station.model, selected_transition)()
        print("Transitioning to state:", charging_station.model.state)
    else:
        print("Invalid transition. Please try again.")
    return True

# Main function to loop until user exits
def main():
    while prompt_for_transition():
        pass

if __name__ == "__main__":
    main()
