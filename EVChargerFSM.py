from transitions import Machine

# Define the states
states = ['Idle', 'Connected', 'Charging', 'Paused', 'Finished', 'Error', 'Maintenance']

# Define transitions with conditions
transitions = [
    {'trigger': 'plug_in_vehicle', 'source': 'Idle', 'dest': 'Connected', 'conditions': 'vehicle_plugged_in'},
    {'trigger': 'unplug_vehicle', 'source': 'Connected', 'dest': 'Idle', 'conditions': 'vehicle_unplugged'},
    {'trigger': 'ready_for_charging', 'source': 'Connected', 'dest': 'Charging', 'conditions': 'ready_for_charging'},
    {'trigger': 'charging_complete', 'source': 'Charging', 'dest': 'Finished', 'conditions': 'charging_complete'},
    {'trigger': 'pause_charging', 'source': 'Charging', 'dest': 'Paused', 'conditions': 'pause_charging'},
    {'trigger': 'resume_charging', 'source': 'Paused', 'dest': 'Charging', 'conditions': 'resume_charging'},
    {'trigger': 'charging_error', 'source': 'Paused', 'dest': 'Error', 'conditions': 'charging_error'},
    {'trigger': 'address_error', 'source': 'Error', 'dest': 'Maintenance', 'conditions': 'address_error'},
    {'trigger': 'finish_maintenance', 'source': 'Maintenance', 'dest': 'Idle', 'conditions': 'finish_maintenance'},
    {'trigger': 'unplug_vehicle_finished', 'source': 'Finished', 'dest': 'Idle', 'conditions': 'vehicle_unplugged'},
]

# Define the outputs for each transition
outputs = {
    'vehicle_plugged_in': 'User Plugs in Vehicle',
    'vehicle_unplugged': 'Vehicle is unplugged by user',
    'ready_for_charging': 'Vehicle is ready for charging',
    'charging_complete': 'Vehicle’s battery is charged to max state possible by the car',
    'pause_charging': 'User pauses charging through the EV charging station app',
    'resume_charging': 'User resumes charging through the EV charging station app',
    'charging_error': 'Error pops up when charging',
    'address_error': 'Enters maintenance mode to address error',
    'finish_maintenance': 'Finished maintenance'
}

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
        else:
            print("Invalid transition. Please try again.")

if __name__ == "__main__":
    main()
