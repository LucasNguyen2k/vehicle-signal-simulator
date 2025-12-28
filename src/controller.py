# SDV Brain
from src.vehicle_state import VehicleState

class VehicleController:
    def __init__(self, state: VehicleState):
        self.state = state

    def can_drive(self) -> bool:
        # Simple logic: can drive if battery > 20% and no door is open
        signals = self.state.snapshot()
        
        if signals.door_open:
            return False
        if signals.gear_name != "D":
            return False
        if signals.battery_percent <= 5:
            return False
        return True
    