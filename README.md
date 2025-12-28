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
    │
    └───tests
        │   test_can_processor.py
        │   test_controller.py
        │   test_signals.py
        │   test_validator.py
        │   test_vehicle_state.py

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




    │   README.md
    │   requirements.txt
    │   
    ├───.pytest_cache
    │   │   .gitignore
    │   │   CACHEDIR.TAG
    │   │   README.md
    │
    ├───src
    │   │   can_message.py
    │   │   can_processor.py
    │   │   controller.py
    │   │   signals.py
    │   │   validator.py
    │   │   vehicle_state.py
    │
    └───tests
        │   test_can_processor.py
        │   test_controller.py
        │   test_signals.py
        │   test_validator.py
        │   test_vehicle_state.py
        