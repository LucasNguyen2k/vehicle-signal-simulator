from src.vehicle_state import VehicleState
from src.controller import VehicleController

def test_vehicle_can_drive():
    state = VehicleState()
    state.update(battery_percent=50.0, door_open=False, gear_name="D")

    controller = VehicleController(state)
    assert controller.can_drive() is True

def test_vehicle_cannot_drive_with_door_open():
    state = VehicleState()
    state.update(battery_percent=50.0, door_open=True, gear_name="D")

    controller = VehicleController(state)
    assert controller.can_drive() is False


    