import pandas as pd

class SmartCAN:
    """Class to handle ADAS data validation and AI diagnostics."""
    
    def __init__(self):
        # Simulated Technical Manual (RAG context)
        self.manual = {
            "ERR_TIMEOUT": "Inconsistent signal: Check CAN bus wiring and Radar sensor."
        }

    def validate_data(self, df):
        """QA Layer: Check if distance is physically possible."""
        # If distance is negative, it's a sensor/data error
        errors = df[df['Distance_m'] < 0]
        return errors

    def get_ai_report(self, status_code):
        """Simulates AI analyzing the fault."""
        detail = self.manual.get(status_code, "Unknown system error.")
        return f"AI Diagnosis: {detail}"