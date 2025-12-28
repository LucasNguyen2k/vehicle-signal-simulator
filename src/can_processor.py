class CANProcessor:
    def parse(self, message):
        if not isinstance(message.data, dict):
            raise ValueError("Invalid CAN payload")
        
        return {
            "speed": message.data.get("speed", 0),
            "rpm": message.data.get("rpm", 0),
            "gear": message.data.get("gear", 0)
        }
    