"""
Docstring for src.
    Vehicle States {
        OFF
        BOOTING
        IDLE
        DRIVING
        ERROR
    }
    
    Events {
        power_on
        boot_complete
        start_drive
        stop_drive
        fault
        reset
    }
"""

class InvalidTransition(Exception):
    pass


class VehicleStateMachine:
    def __init__(self):
        self.state = "OFF"

    def handle_event(self, event: str):
        transitions = {
            "OFF": {"power_on": "BOOTING"},
            "BOOTING": {"boot_complete": "IDLE", "fault": "ERROR"},
            "IDLE": {"start_drive": "DRIVING", "fault": "ERROR"},
            "DRIVING": {"stop_drive": "IDLE", "fault": "ERROR"},
            "ERROR": {"reset": "OFF"},
        }

        if event not in transitions.get(self.state, {}):
            raise InvalidTransition(
                f"Cannot handle event '{event}' in state '{self.state}'"
            )

        self.state = transitions[self.state][event]
        return self.state
