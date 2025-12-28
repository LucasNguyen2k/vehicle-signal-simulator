from src.signals import VehicleSignal

class VehicleState:
    def __init__(self):
        self.signal = VehicleSignal()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if not hasattr(self.signal, key):
                raise ValueError(f"Invalid signal attribute: {key}")
            else:
                setattr(self.signal, key, value)

    def snapshot(self) -> VehicleSignal:
        return self.signal
        