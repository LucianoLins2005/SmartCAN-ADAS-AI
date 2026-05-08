import streamlit as st
import pandas as pd
import time
from src.main import SmartCAN

# Page Configuration
st.set_page_config(page_title="SmartCAN Analyzer - Stellantis", layout="wide")
analyzer = SmartCAN()

st.title("🚗 SmartCAN Analyzer: ADAS AI Validation")
st.markdown("---")

# 1. Data Simulation
data = {
    'Timestamp': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
    'Distance_m': [50.5, 48.2, -99.0, 42.1, 40.5, 38.0],
    'Status': ['OK', 'OK', 'ERR_TIMEOUT', 'OK', 'OK', 'OK']
}
df = pd.DataFrame(data)

# 2. Telemetry Visualization (THE CHART)
st.subheader("📊 Real-time Telemetry Visualization")
# Using st.area_chart for better visual impact of the signal drop
st.area_chart(df.set_index('Timestamp')['Distance_m'])
st.caption("Figure 1: Distance sensor telemetry. The sharp drop to -99.0 indicates a critical signal failure (Timeout).")

st.markdown("---")

# 3. Data Table and Analysis
col1, col2 = st.columns([2, 1])

with col1:
    st.write("**CAN Bus Raw Data (via COM API):**")
    st.dataframe(df.style.highlight_min(subset=['Distance_m'], color='#ff4b4b'))

with col2:
    st.metric(label="System Health", value="66%", delta="-34% Failure Detected")
    if st.button("Run AI Diagnostic"):
        with st.spinner('AI analyzing engineering context...'):
            time.sleep(1)
            
            # QA Logic
            is_valid, anomalies = analyzer.validate_data(df)
            if not is_valid:
                st.error(f"⚠️ QA ALERT: Physical inconsistency at {anomalies['Timestamp'].values[0]}s.")
            
            # AI Diagnosis
            report = analyzer.get_ai_report("ERR_TIMEOUT")
            st.info(f"🤖 **{report}**")
            st.success("✅ **Recommendation:** Inspect harness connector C1 for intermittent contact.")

st.markdown("---")
st.caption("Proprietary Tool for Automotive Validation - Stellantis Project")