class SignalValidator:
    def validatate(self, signal):
        errors = []
        if not (0 <= signal.speed_kmh <= 300):
            errors.append("Speed must be between 0 and 300 km/h.")

        if not (0 <= signal.rpm <= 8000):
            errors.append("RPM must be between 0 and 8000.")

        if not (0 <= signal.battery_percent <= 100):
            errors.append("Battery percentage must be between 0 and 100%.")

        if not (-40 <= signal.temperature_c <= 125):
            errors.append("Temperature must be between -40 and 125 Celsius.")
        
        return errors

