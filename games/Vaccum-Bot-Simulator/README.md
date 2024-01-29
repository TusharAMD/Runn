# Vacuum Bot Simulator

Welcome to the **Vacuum Bot Simulator**! In this simulation, you control a virtual vacuum bot (vbot) as it navigates through a room to clean up dirt piles. The vbot has a limited battery that depletes as it moves around the room.

## How to Run
1. This program MUST be run in a Terminal/Command Prompt window.
2. Install the required `bext` module by following the instructions at [https://pypi.org/project/Bext/](https://pypi.org/project/Bext/).
3. Run the provided Python script.

## Simulation Features
- The room is represented in the terminal window with dirt piles, the vacuum bot (vbot), and a base station.
- The vbot moves towards dirt piles, cleans them, and returns to the base station to recharge.
- The vbot has a charging status indicator and a battery percentage display.
- The simulation includes dynamic dirt addition to the room over time.

## Controls
- Press `Ctrl-C` to quit the simulation.

## Customization
- Experiment with the simulation by adjusting the following parameters in the script:
  - `DIRT_ADD_FREQUENCY`: Frequency of dirt addition.
  - `DIRT_ADD_AMOUNT`: Amount of dirt added each time.
  - `NUM_STARTING_DIRT`: Initial number of dirt piles.
  - `MAX_BATTERY`: Maximum battery capacity.
  - `RECHARGE_RATE`: Rate of battery recharge.
  - `PAUSE`: Simulation pause time.

Feel free to explore the virtual world of the Vacuum Bot Simulator! 🤖🧹
