import time
from src.can_message import CANMessage
from src.can_processor import CANProcessor

def test_can_message_parsing():
    processor = CANProcessor()
    message = CANMessage(
        arbitration_id=0x100,
        data={
            "speed": 100,
            "rpm": 3000,
            "gear": 4
        },
        timestamp=time.time()
    )
    result = processor.parse(message)
    assert result["speed"] == 100
    assert result["rpm"] == 3000
    assert result["gear"] == 4