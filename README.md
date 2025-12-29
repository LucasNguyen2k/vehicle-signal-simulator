# Software-Defined Vehicle (SDV) – Vehicle Signal Simulation and Validation

## Overview
Built a software-defined vehicle simulation platform with signal services, OTA update flows, diagnostics, and CI-driven safety validation

This SDV project series demonstrates:
- A signal publisher (speed, RPM, battery)
- A consumer (ADAS / monitoring service)
- Validation & fault injection
- CI tests for safety rules
- Test-driven development
- Automation and Mocking

The Vehicle Signal Service focuses on:
-	Simulates vehicle signals (speed, RPM, battery, temperature)
-	Validates signal correctness
-	Detects abnormal conditions
-	Is fully testable
-	Runs in CI

## Tech Stack
- Python 3.10+
- dataclasses
- pytest

## Project Structure
```text

SDVProjects/
└── vehicle-signal-simulator/
    │   README.md
    │   requirements.txt
    │
    ├───src
    │   │   can_message.py
    │   │   can_processor.py
    │   │   controller.py
    │   │   signals.py
    │   │   validator.py
    │   │   vehicle_state.py
    │   │   state_machine.py
    │
    └───tests
        │   test_can_processor.py
        │   test_controller.py
        │   test_signals.py
        │   test_validator.py
        │   test_vehicle_state.py
```


## Vehicle State Machine Diagram
```
digraph {
        OFF [label=OFF]
        BOOTING [label=BOOTING]
        IDLE [label=IDLE]
        DRIVING [label=DRIVING]
        ERROR [label=ERROR color=red]
        OFF -> BOOTING [label=power_on]
        BOOTING -> IDLE [label=boot_complete]
        BOOTING -> ERROR [label=fault]
        IDLE -> DRIVING [label=start_drive]
        IDLE -> ERROR [label=fault]
        DRIVING -> IDLE [label=stop_drive]
        DRIVING -> ERROR [label=fault]
        ERROR -> OFF [label=reset]
}
```
## Installation
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt

## Outputs:
None

## Testing
```
python -m pytest
```