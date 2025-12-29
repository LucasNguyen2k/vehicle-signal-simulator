import pytest
from src.state_machine import VehicleStateMachine, InvalidTransition

def test_normal_drive_flow():
    vsm = VehicleStateMachine()

    assert vsm.handle_event("power_on") == "BOOTING"
    assert vsm.handle_event("boot_complete") == "IDLE"
    assert vsm.handle_event("start_drive") == "DRIVING"
    assert vsm.handle_event("stop_drive") == "IDLE"

def test_fault_transition():
    vsm = VehicleStateMachine()
    vsm.handle_event("power_on")

    assert vsm.handle_event("fault") == "ERROR"
    assert vsm.handle_event("reset") == "OFF"

def test_invalid_transition_raises():
    vsm = VehicleStateMachine()

    with pytest.raises(InvalidTransition):
        vsm.handle_event("start_drive")
