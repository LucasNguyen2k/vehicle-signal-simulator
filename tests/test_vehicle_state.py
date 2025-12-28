import pytest
from src.vehicle_state import VehicleState

def test_update_vehicle_state():
    vehicle = VehicleState()
    vehicle.update(speed_kmh=50, rpm=2000)

    assert vehicle.signal.speed_kmh == 50
    assert vehicle.signal.rpm == 2000

def test_invalid_signal_raises():
    vehicle = VehicleState()
    with pytest.raises(ValueError):
        vehicle.update(fuel=50)  # 'fuel' is not a valid attribute
    
    
    
    