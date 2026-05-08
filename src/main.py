import pandas as pd
from typing import Tuple

class SmartCAN:
    """
    Intelligent Validation System for ADAS Telemetry.
    Integrates physical constraints with AI-driven diagnostics.
    """
    
    def __init__(self):
        # Technical Knowledge Base (Simulating RAG context)
        self._knowledge_base = {
            "ERR_TIMEOUT": "Signal loss detected. Inspect CAN harness and Radar alignment.",
            "ERR_PHYSICAL": "Physical inconsistency. Sensor reading out of safety bounds."
        }

    def validate_data(self, df: pd.DataFrame) -> Tuple[bool, pd.DataFrame]:
        """
        QA Layer: Validates if distance values are physically possible.
        Returns a boolean for status and a dataframe of detected anomalies.
        """
        # Strict validation: Distance must be between 0 and 200 meters
        anomalies = df[(df['Distance_m'] < 0) | (df['Distance_m'] > 200)]
        is_valid = anomalies.empty
        return is_valid, anomalies

    def get_ai_report(self, error_code: str) -> str:
        """Fetch expert diagnostic based on error signature."""
        return self._knowledge_base.get(error_code, "Unknown system anomaly.")