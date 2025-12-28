from dataclasses import dataclass

@dataclass
class VehicleSignal:        # AUTOSAR/VSS style vehicle signals
    speed_kmh: float = 0.0  # Speed in km/h
    rpm: int = 0            # Revolutions per minute
    gear: int = 0           # Current gear
    gear_name: str = "P"    # Gear name (e.g., P, R, N, D)
    throttle: float = 0.0   # 0.0 - 1.0 Throttle position percentage
    brake: float = 0.0      # 0.0 - 1.0 brake application
    battery_percent: float = 100.0  # Battery percentage
    temperature_c: float = 0.0  # Temperature in Celsius
    door_open: bool = False  # Is any door open

