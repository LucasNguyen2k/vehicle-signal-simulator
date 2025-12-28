from src.signals import VehicleSignal

def test_vehicle_signal_creation():
    signal = VehicleSignal(speed_kmh=100,
                           rpm=3000, 
                           battery_percent=80.0, 
                           temperature_c=25
                           )
    assert signal.speed_kmh == 100
    assert signal.rpm == 3000
    assert signal.battery_percent == 80.0
    assert signal.temperature_c == 25

def test_default_vehicle_signal():
    signals = VehicleSignal()
    assert signals.speed_kmh == 0.0
    assert signals.rpm == 0
    assert signals.gear == 0
    assert signals.throttle == 0.0
    assert signals.brake == 0.0
    assert signals.battery_percent == 100.0
    assert signals.temperature_c == 0.0

