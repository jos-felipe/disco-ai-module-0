# Expert System Project - Discovery Piscine AI/ML

## Overview
This project implements a simple expert system that regulates indoor temperature based on outdoor temperature fluctuations. It consists of two main components:

1. **Environment Simulator (`environment.py`)**: Simulates outdoor temperature throughout the day for different seasons.
2. **Expert System (`expert_system.py`)**: Controls heating and cooling systems to maintain indoor temperature within a comfortable range.

## What is an Expert System?
An expert system is a basic type of artificial intelligence that uses predefined rules and knowledge to simulate decision-making. It operates within a state machine paradigm, where the system can only be in one specific state at a time, with external events triggering state changes.

## Requirements
- Python 3.x

## Usage

### Environment Simulator
Simulates outdoor temperature variations throughout a day:

```bash
python environment.py <season>
```

Where `<season>` can be:
- "winter", "spring", "summer", "autumn" (as text)
- 1, 2, 3, 4 (as numbers representing winter, spring, summer, autumn)

The program outputs temperature values every second, with each second representing a 30-minute interval in the simulation (48 seconds = 24 hours).

### Expert System
Takes input temperatures and manages heating/cooling to maintain comfort:

```bash
python environment.py <season> | python expert_system.py <min_comfort> <max_comfort>
```

Where:
- `<min_comfort>`: Lower threshold of the comfort zone temperature
- `<max_comfort>`: Upper threshold of the comfort zone temperature

## How It Works

### Environment Simulator
- Uses a sine wave to model daily temperature fluctuations
- Adjusts temperature ranges based on the selected season
- Adds small random variations for realism
- Outputs one temperature value per second

### Expert System
- Reads outdoor temperature values from standard input
- Initially sets indoor temperature equal to outdoor temperature
- Activates heating when temperature falls below minimum comfort level
- Activates cooling when temperature exceeds maximum comfort level
- When active, heating increases indoor temperature by 0.5°C per cycle
- When active, cooling decreases indoor temperature by 0.5°C per cycle
- When inactive, indoor temperature gradually moves toward outdoor temperature (±0.25°C per cycle)
- Outputs current state: `<external_temp> - <action> - <indoor_temp>`

## Example Output
```
7.5 - heating - 8.0
8.0 - heating - 9.0
8.5 - heating - 10.0
9.0 - heating - 11.0
10.0 - heating - 12.5
11.0 - heating - 14.0
12.0 - nothing - 13.75
13.25 - nothing - 13.5
14.5 - nothing - 13.75
15.0 - nothing - 14.0
15.5 - nothing - 14.25
15.5 - nothing - 14.5
15.5 - nothing - 14.75
16.0 - nothing - 15.0
16.0 - cooling - 14.5
15.5 - cooling - 13.5
15.5 - nothing - 13.75
```

## Project Structure
```
ai-ml_discovery/
└── module0/
    ├── environment.py
    └── expert_system.py
```

## Learning Objectives
- Understanding basic AI concepts
- Implementing state machines 
- Working with rule-based systems
- Creating simulations with Python

## Implementation Details

### Environment Simulator
- Temperature is modeled as a sine wave with season-specific parameters
- The sine wave is shifted so that temperatures are lowest around 5 AM 
- The amplitude is calculated based on seasonal min/max temperatures
- Random variations are added for more realistic simulation

### Expert System
- Uses simple threshold-based rules to determine system state
- Implements gradual heating/cooling effects
- Models temperature inertia when systems are inactive
- Outputs the current state for monitoring purposes
