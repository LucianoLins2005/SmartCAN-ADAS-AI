import streamlit as st
import pandas as pd
import plotly.express as px
import time
from src.main import SmartCAN

# 1. Professional Page Setup
st.set_page_config(page_title="SmartCAN Analyzer - Stellantis", layout="wide")
analyzer = SmartCAN()

st.title("🚗 SmartCAN Analyzer: ADAS AI Validation")
st.markdown("""
    **Engineering Brief:** Real-time ADAS telemetry monitoring for signal integrity and AI diagnostics.
""")
st.markdown("---")

# 2. Technical Data Simulation
data = {
    'Timestamp (s)': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
    'Distance_m': [50.5, 48.2, -99.0, 42.1, 40.5, 38.0], # Critical failure
    'Status': ['OK', 'OK', 'ERR_TIMEOUT', 'OK', 'OK', 'OK']
}
df = pd.DataFrame(data)

# 3. RESPONSIVE VISUALIZATION (Using Plotly)
st.subheader("📊 Interactive Telemetry Analysis")

# Criando o gráfico responsivo com Plotly
fig = px.line(df, x='Timestamp (s)', y='Distance_m', 
              title='ADAS Sensor Telemetry: Frontal Distance Over Time',
              markers=True, 
              labels={'Distance_m': 'Distance (Meters)', 'Timestamp (s)': 'Time (Seconds)'})

# Customizando a estética para o padrão Stellantis
fig.update_traces(line_color='#007bff', marker=dict(size=10))
fig.add_annotation(x=0.3, y=-99, text="CRITICAL SIGNAL DROP",
                   showarrow=True, arrowhead=1, ax=40, ay=-40, arrowcolor="red", font=dict(color="red"))

# Garante que o gráfico ocupe 100% da largura disponível e seja responsivo
st.plotly_chart(fig, use_container_width=True)

st.caption("Figure 1: Responsive telemetry log. This chart automatically resizes with your browser window.")

st.markdown("---")

# 4. Data Inspection and AI Diagnosis
col1, col2 = st.columns([2, 1])

with col1:
    st.write("**CAN Bus Raw Logs:**")
    st.dataframe(df.style.highlight_min(subset=['Distance_m'], color='#ff4b4b'), use_container_width=True)

with col2:
    st.metric(label="System Reliability Index", value="66%", delta="-34% Anomaly")
    
    if st.button("Generate AI Diagnostic Report"):
        with st.spinner('Analyzing...'):
            time.sleep(1)
            is_valid, anomalies = analyzer.validate_data(df.rename(columns={'Timestamp (s)': 'Timestamp'}))
            if not is_valid:
                st.error(f"⚠️ **QA ALERT:** Physical constraint violated.")
            report = analyzer.get_ai_report("ERR_TIMEOUT")
            st.info(f"🤖 **AI Verdict:** {report}")
            st.success("✅ **Recommendation:** Inspect harness connector C1.")