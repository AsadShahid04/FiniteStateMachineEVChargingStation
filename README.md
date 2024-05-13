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
