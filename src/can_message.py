from dataclasses import dataclass

@dataclass
class CANMessage:
    arbitration_id: int
    data: dict
    timestamp: float

{
    "speed": 80,
    "rpm": 3000,
    "gear": 4
}