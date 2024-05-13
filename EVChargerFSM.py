from transitions import Machine
from transitions.extensions import GraphMachine

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
        'outputs': ['Finished', 'Paused'],
        'transitions': ['charging_complete', 'pause_charging']
    },
    'Paused': {
        'outputs': ['Error', 'Charging'],
        'transitions': ['charging_error', 'resume_charging']
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
    def __init__(self):
        self.plugged_in = False
        self.charging = False
        self.error = False

    def plug_in_vehicle(self):
        if self.state == 'Idle':
            self.state = 'Connected'
            print("User Plugs in Vehicle. Transitioning to Connected state.")
        else:
            print("Vehicle is already plugged in.")

    def unplug_vehicle(self):
        if self.state == 'Connected':
            self.state = 'Idle'
            print("Vehicle is unplugged by user. Transitioning to Idle state.")
        else:
            print("No vehicle is currently connected.")

    def ready_for_charging(self):
        if self.state == 'Connected':
            self.state = 'Charging'
            print("Vehicle is ready for charging. Transitioning to Charging state.")
        else:
            print("Vehicle is not in the correct state for charging.")

    def charging_complete(self):
        if self.state == 'Charging':
            self.state = 'Finished'
            print("Vehicle's battery is charged to max state possible by the car. Transitioning to Finished state.")
        else:
            print("Charging is not in progress.")

    def pause_charging(self):
        if self.state == 'Charging':
            self.state = 'Paused'
            print("User pauses charging through the EV charging station app. Transitioning to Paused state.")
        else:
            print("Charging is not in progress.")

    def resume_charging(self):
        if self.state == 'Paused':
            self.state = 'Charging'
            print("User resumes charging through the EV charging station app. Transitioning to Charging state.")
        else:
            print("Charging is not paused.")

    def charging_error(self):
        if self.state == 'Paused':
            self.state = 'Error'
            print("Error pops up when charging. Transitioning to Error state.")
        else:
            print("No error occurred during charging.")

    def address_error(self):
        if self.state == 'Error':
            self.state = 'Maintenance'
            print("Enters maintenance mode to address error. Transitioning to Maintenance state.")
        else:
            print("No error to address.")

    def finish_maintenance(self):
        if self.state == 'Maintenance':
            self.state = 'Idle'
            print("Finished maintenance. Transitioning to Idle state.")
        else:
            print("Maintenance is not required.")

    def unplug_vehicle_finished(self):
        if self.state == 'Finished':
            self.state = 'Idle'
            print("Vehicle is unplugged by the user. Transitioning to Idle state.")
        else:
            print("Vehicle is not in a finished charging state.")
            
charging_station = GraphMachine(model=EVCharger(), states=list(state_info.keys()), initial='Idle', send_event=True, queued=True)

# Add transitions and outputs to the state machine
for state, info in state_info.items():
    for transition, dest in zip(info['transitions'], info['outputs']):
        charging_station.add_transition(trigger=transition, source=state, dest=dest)

# Function to prompt user for input and transition to the next state
def prompt_for_transition():

    # Get the transitions for the current state
    current_state = charging_station.model.state
    available_transitions = state_info[current_state]['transitions']
    print ("\n")
    print("Transitions for " + current_state +  " state are:", available_transitions)
    # print("Current state:", current_state)
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
        
    # Save the state machine graph
    charging_station.get_graph().draw("state_machine.png", prog="dot", format="png")
    print("Finite machine graph saved as state_machine.png")

if __name__ == "__main__":
    main()
