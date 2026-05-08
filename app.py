import streamlit as st
import pandas as pd
from src.main import SmartCAN # Importa a lógica que criamos acima

# Setup
st.set_page_config(page_title="SmartCAN Dashboard", layout="wide")
analyzer = SmartCAN()
# Adicione isso logo após mostrar a tabela no app.py
st.subheader("📊 Telemetry Visualization")
st.line_chart(df.set_index('Timestamp')['Distance_m'])
st.caption("Visual representation of sensor distance over time. Note the sharp drop representing the detected anomaly.")
st.title("🚗 Stellantis SmartCAN - ADAS AI Validation")

# ... (mantenha o início do seu código app.py igual)

# 1. Input Simulation (The Problem)
st.subheader("📡 Real-time CAN Bus Telemetry")

# Gráfico de Linha para Visualização de Sinais (ADICIONE ISTO)
st.line_chart(df.set_index('Timestamp')['Distance_m'])
st.caption("Visual representation of sensor distance over time. Note the sharp drop at 0.3s.")

col1, col2 = st.columns([2, 1])
# ... (restante do código com a tabela e o botão)

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

    