import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
from src.main import SmartCAN

# 1. Professional Page Setup
st.set_page_config(page_title="SmartCAN Analyzer - Stellantis", layout="wide")
analyzer = SmartCAN()

st.title("🚗 SmartCAN Analyzer: ADAS AI Validation")
st.markdown("""
    **Engineering Brief:** This dashboard monitors real-time ADAS telemetry logs to identify 
    signal dropouts and generate AI-driven root-cause diagnostics for safety validation.
""")
st.markdown("---")

# 2. Technical Data Simulation
data = {
    'Timestamp (s)': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
    'Distance_m': [50.5, 48.2, -99.0, 42.1, 40.5, 38.0], # Critical failure at 0.3s
    'Status': ['OK', 'OK', 'ERR_TIMEOUT', 'OK', 'OK', 'OK']
}
df = pd.DataFrame(data)

# 3. ADVANCED TELEMETRY VISUALIZATION (Matplotlib Version)
st.subheader("📊 Advanced Telemetry Analysis")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['Timestamp (s)'], df['Distance_m'], marker='o', linestyle='-', color='#007bff', label='Frontal Radar Distance')

# Professional Axis Nomenclature
ax.set_title('ADAS Sensor Telemetry: Frontal Distance Over Time', fontsize=12, fontweight='bold')
ax.set_xlabel('Time (Seconds)', fontsize=10)
ax.set_ylabel('Distance to Target (Meters)', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# Expert Annotation for the Manager
ax.annotate('CRITICAL SIGNAL DROP', xy=(0.3, -99), xytext=(0.4, -60),
             arrowprops=dict(facecolor='red', shrink=0.05),
             color='red', fontweight='bold')

# Setting Y-axis limits to show the drop clearly
ax.set_ylim(-110, 70)

st.pyplot(fig)
st.caption("Figure 1: High-fidelity telemetry log. The red annotation indicates a physically impossible signal dropout.")

st.markdown("---")

# 4. Data Inspection and AI Diagnosis
col1, col2 = st.columns([2, 1])

with col1:
    st.write("**CAN Bus Raw Logs:**")
    # Highlight the specific row of failure
    st.dataframe(df.style.highlight_min(subset=['Distance_m'], color='#ff4b4b'), use_container_width=True)

with col2:
    st.metric(label="System Reliability Index", value="66%", delta="-34% Anomaly Detected")
    
    if st.button("Generate AI Diagnostic Report"):
        with st.spinner('Accessing engineering knowledge base...'):
            time.sleep(1.2)
            
            # QA Logic Validation
            is_valid, anomalies = analyzer.validate_data(df.rename(columns={'Timestamp (s)': 'Timestamp'}))
            
            if not is_valid:
                st.error(f"⚠️ **QA ALERT:** Physical constraint violated at {anomalies['Timestamp'].values[0]}s.")
            
            # AI Inference
            report = analyzer.get_ai_report("ERR_TIMEOUT")
            st.info(f"🤖 **AI Verdict:** {report}")
            st.success("✅ **Recommendation:** Inspect harness connector C1 and check Radar sensor alignment.")

st.markdown("---")
st.caption("Proprietary Tool for Stellantis ADAS Validation - AI Product Analyst Portfolio")