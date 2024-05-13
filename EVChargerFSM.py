from transitions import Machine

# Define the states
states = ['Idle', 'Connected', 'Charging', 'Paused', 'Finished', 'Error', 'Maintenance']

# Define transitions
transitions = [
    {'trigger': 'plug_in_vehicle', 'source': 'Idle', 'dest': 'Connected'},
    {'trigger': 'unplug_vehicle', 'source': 'Connected', 'dest': 'Idle'},
    {'trigger': 'ready_for_charging', 'source': 'Connected', 'dest': 'Charging'},
    {'trigger': 'charging_complete', 'source': 'Charging', 'dest': 'Finished'},
    {'trigger': 'pause_charging', 'source': 'Charging', 'dest': 'Paused'},
    {'trigger': 'resume_charging', 'source': 'Paused', 'dest': 'Charging'},
    {'trigger': 'charging_error', 'source': 'Paused', 'dest': 'Error'},
    {'trigger': 'address_error', 'source': 'Error', 'dest': 'Maintenance'},
    {'trigger': 'finish_maintenance', 'source': 'Maintenance', 'dest': 'Idle'},
    {'trigger': 'unplug_vehicle', 'source': 'Finished', 'dest': 'Idle'},
]

# Define the EV Charging Station class
class EVChargingStation(object):
    def __init__(self):
        self.machine = Machine(model=self, states=states, transitions=transitions, initial='Idle')

def main():
    # Create an instance of EVChargingStation
    charging_station = EVChargingStation()

    # Display available transitions
    print(f"Current state: {charging_station.state}")
    print(f"Available transitions from '{charging_station.state}': {charging_station.machine.get_triggers()}")

    # Prompt for user input
    while True:
        print("Select a transition (type 'exit' to quit):")
        selected_transition = input("> ")

        if selected_transition == 'exit':
            break

        if selected_transition in charging_station.machine.get_triggers():
            getattr(charging_station, selected_transition)()
            print(f"Transitioning to state: {charging_station.state}")
            print(f"Available transitions from '{charging_station.state}': {charging_station.machine.get_triggers()}")
        else:
            print("Invalid transition. Please try again.")

if __name__ == "__main__":
    main()
