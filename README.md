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
    ├── src/
    │   ├── __init__.py
    │   ├── signals.py
    │   └── validator.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_signals.py
    │   └── test_validator.py
    ├── requirements.txt
    └── README.md

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



