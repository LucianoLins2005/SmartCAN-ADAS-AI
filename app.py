import streamlit as st
import pandas as pd
from src.main import SmartCAN # Importa a lógica que criamos acima

# Setup
st.set_page_config(page_title="SmartCAN Dashboard", layout="wide")
analyzer = SmartCAN()

st.title("🚗 Stellantis SmartCAN - ADAS AI Validation")

# 1. Simulate CAN Bus Data (The Problem)
data = {
    'Timestamp': [0.1, 0.2, 0.3, 0.4],
    'Distance_m': [50.5, 48.2, -99.0, 42.1], # -99.0 is the simulated error
    'Status': ['OK', 'OK', 'ERR_TIMEOUT', 'OK']
}
df = pd.DataFrame(data)

st.subheader("CAN Bus Telemetry")
st.dataframe(df)

# 2. Run Validation
if st.button("Run AI Diagnostic"):
    st.markdown("### Analysis Results")
    
    # QA Check
    anomalies = analyzer.validate_data(df)
    if not anomalies.empty:
        st.error(f"QA Alert: Invalid physical data at {anomalies['Timestamp'].values[0]}s.")
        
    # AI Report
    report = analyzer.get_ai_report("ERR_TIMEOUT")
    st.info(report)
    st.success("Recommendation: Inspect harness connector C1.")