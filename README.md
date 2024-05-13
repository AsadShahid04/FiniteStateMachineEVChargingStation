# EV Charging Station FSM

This Python script implements a Finite State Machine (FSM) model for an Electric Vehicle (EV) Charging Station. It uses the `transitions` library to define states, transitions, and outputs for the charging station.

## Usage

1. Make sure you have Python installed on your system.

2. Install the `transitions` library using pip:

   ```
   pip install transitions
   ```

3. Run the `EVChargerFSM.py` script:

   ```
   python EVChargerFSM.py
   ```

4. Follow the prompts to select transitions and interact with the charging station FSM.

## States and Transitions

The charging station FSM has the following states:

- **Idle**: The charger is not currently in use and is waiting for a car to connect.
- **Connected**: A car is connected to the charger, but charging has not begun.
- **Charging**: The charger is supplying power to the car's battery.
- **Paused**: Charging was temporarily stopped, possibly due to some error.
- **Finished**: Charging has been completed, and the vehicle's battery is fully charged.
- **Error**: An error has occurred, such as a fault in the charger or vehicle.
- **Maintenance**: The charger is in maintenance mode, possibly for software updates or diagnostics.

The following transitions are available:

- **Idle → Connected**: User plugs in vehicle.
- **Connected → Idle**: Vehicle is unplugged by user.
- **Connected → Charging**: Vehicle is ready for charging.
- **Charging → Finished**: Vehicle's battery is charged to max state possible.
- **Charging → Paused**: User pauses charging through the EV charging station app.
- **Paused → Charging**: User resumes charging through the EV charging station app.
- **Paused → Error**: Error pops up when charging.
- **Error → Maintenance**: Enters maintenance mode to address error.
- **Maintenance → Idle**: Finished maintenance.
- **Finished → Idle**: Vehicle is unplugged by the user.

## Additional Notes

- This script uses a Mealy Machine model for the charging station FSM.
- Outputs are defined for each transition, providing descriptions of the transitions.

## Document Testing of the FSM [Part 3]

```
Transitions for Idle state are: ['plug_in_vehicle']
Select a transition (type 'exit' to quit): plug_in_vehicle
User Plugs in Vehicle. Transitioning to Connected state.
Transitioning to state: Connected


Transitions for Connected state are: ['unplug_vehicle', 'ready_for_charging']
Select a transition (type 'exit' to quit): unplug_vehicle
Vehicle is unplugged by user. Transitioning to Idle state.
Transitioning to state: Idle


Transitions for Idle state are: ['plug_in_vehicle']
Select a transition (type 'exit' to quit): plug_in_vehicle
User Plugs in Vehicle. Transitioning to Connected state.
Transitioning to state: Connected


Transitions for Connected state are: ['unplug_vehicle', 'ready_for_charging']
Select a transition (type 'exit' to quit): ready_for_charging
Vehicle is ready for charging. Transitioning to Charging state.
Transitioning to state: Charging


Transitions for Charging state are: ['charging_complete', 'pause_charging']
Select a transition (type 'exit' to quit): pause_charging
User pauses charging through the EV charging station app. Transitioning to Paused state.
Transitioning to state: Paused


Transitions for Paused state are: ['charging_error', 'resume_charging']
Select a transition (type 'exit' to quit): resume_charging
User resumes charging through the EV charging station app. Transitioning to Charging state.
Transitioning to state: Charging


Transitions for Charging state are: ['charging_complete', 'pause_charging']
Select a transition (type 'exit' to quit): pause_charging
User pauses charging through the EV charging station app. Transitioning to Paused state.
Transitioning to state: Paused


Transitions for Paused state are: ['charging_error', 'resume_charging']
Select a transition (type 'exit' to quit): charging_error
Error pops up when charging. Transitioning to Error state.
Transitioning to state: Error


Transitions for Error state are: ['address_error']
Select a transition (type 'exit' to quit): address_error
Enters maintenance mode to address error. Transitioning to Maintenance state.
Transitioning to state: Maintenance


Transitions for Maintenance state are: ['finish_maintenance']
Select a transition (type 'exit' to quit): finish_maintenance
Finished maintenance. Transitioning to Idle state.
Transitioning to state: Idle


Transitions for Idle state are: ['plug_in_vehicle']
Select a transition (type 'exit' to quit): plug_in_vehicle
User Plugs in Vehicle. Transitioning to Connected state.
Transitioning to state: Connected


Transitions for Connected state are: ['unplug_vehicle', 'ready_for_charging']
Select a transition (type 'exit' to quit): ready_for_charging
Vehicle is ready for charging. Transitioning to Charging state.
Transitioning to state: Charging


Transitions for Charging state are: ['charging_complete', 'pause_charging']
Select a transition (type 'exit' to quit): charging_complete
Vehicle's battery is charged to max state possible by the car. Transitioning to Finished state.
Transitioning to state: Finished


Transitions for Finished state are: ['unplug_vehicle_finished']
Select a transition (type 'exit' to quit): unplug_vehicle_finshed
Invalid transition. Please try again.


Transitions for Finished state are: ['unplug_vehicle_finished']
Select a transition (type 'exit' to quit): unplug_vehicle_finished
Vehicle is unplugged by the user. Transitioning to Idle state.
Transitioning to state: Idle


Transitions for Idle state are: ['plug_in_vehicle']
Select a transition (type 'exit' to quit): exit
Finite machine graph saved as state_machine.png
```

# Documenting the Finite State Machine Project Journey

Throughout the Finite State Machine (FSM) project, I began on an exhaustive path to study, develop, construct, and test a basic FSM. Below, I summarize the technique, process, and code history used throughout this project:

### Summary of Research Done/Problem Solving Methodology

I got a formal definition and instruction on the concept of FSM through the website “Finite-State Machine”. I watched the video “Robots vs. Jellybeans: Finite State Automata in Action”, by Peeja, which introduced me to the idea of states using red and green jelly beans. The video helped me understand the finite states a machine can take, a core concept for FSM. These machines also take on the name of automatons. The video also went over the concept of jail if an unexpected state was to be selected. In the video “Finite State Machines explained” by Abelardo Pardo, I reviewed an example of a Moore FSM version of a stop sign and a Mealy FSM version of a stop sign. We could compare and contrast the two types of FSM and their designs/diagrams.

### Type of Finite State Machine (FSM) Used

I decided to use the Mealy Machine type of Finite State Machine (FSM). The Mealy Machine is characterized by its ability to have input-dependent output. The output is determined by both its present state as well as by the input the FTM receives. In accordance with an EV charging station, we can see that the output (charging status, errors, or completion) is determined by both the current state of the machine (idle, charging, paused) as well as by the input provided (plugged-in, starting charging, pause charging, etc).
Dynamic behavior is also relevant to a Mealy Machine type of FSM. This means these machines can display more complicated and dynamic behavior than other types of FSM. This is ideal for EV charging stations as they need to be able to respond to a variety of events/user interactions.

Real-time reaction allows Mealy machines to generate output in response to real-time input events. In contrast, a Moore Machine would only be able to output a state based solely on the current state of itself. This is not suitable specifically for EV charging stations in the real world. Hence, it is more beneficial for us to use a Mealy Machine FSM, which allows us to be more flexible and handle various scenarios that might be thrown based on the EV or the user.
