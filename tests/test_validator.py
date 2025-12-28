from src.signals import VehicleSignal
from src.validator import SignalValidator

def test_valid_signal_passes():
    signal = VehicleSignal(speed_kmh=80,
                           rpm=2000,
                           battery_percent=60.0,
                           temperature_c=30)

    validator = SignalValidator()

    errors = validator.validatate(signal)
    assert len(errors) == 0
    
def test_invalid_speed_detected():
    signal = VehicleSignal(speed_kmh=400,
                           rpm=2000,
                           battery_percent=60.0,
                           temperature_c=30)

    validator = SignalValidator()
    errors = validator.validatate(signal)
    assert "Speed must be between 0 and 300 km/h." in errors

    
