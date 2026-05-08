import streamlit as st
import pandas as pd
import time
from src.main import SmartCAN

# 1. Configuração Inicial
st.set_page_config(page_title="SmartCAN Analyzer - Stellantis", layout="wide")
analyzer = SmartCAN()

st.title("🚗 SmartCAN Analyzer: ADAS AI Validation")
st.markdown("---")

# 2. Simulação de Dados (O Problema)
data = {
    'Timestamp': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
    'Distance_m': [50.5, 48.2, -99.0, 42.1, 40.5, 38.0], # Falha no 0.3s
    'Status': ['OK', 'OK', 'ERR_TIMEOUT', 'OK', 'OK', 'OK']
}
df = pd.DataFrame(data)

# 3. VISUALIZAÇÃO DO GRÁFICO (IMEDIATAMENTE APÓS O TÍTULO)
st.subheader("📊 Real-time Telemetry Visualization")
# Criamos o gráfico usando o Timestamp como índice
chart_data = df.set_index('Timestamp')['Distance_m']
st.area_chart(chart_data)
st.caption("Figure 1: Distance sensor telemetry. Note the sharp drop at 0.3s representing a signal failure.")

st.markdown("---")

# 4. Tabela e Diagnóstico
col1, col2 = st.columns([2, 1])

with col1:
    st.write("**CAN Bus Raw Data:**")
    st.dataframe(df.style.highlight_min(subset=['Distance_m'], color='#ff4b4b'))

with col2:
    st.metric(label="System Health", value="66%", delta="-34% Failure")
    if st.button("Run AI Diagnostic"):
        with st.spinner('AI analyzing...'):
            time.sleep(1)
            is_valid, anomalies = analyzer.validate_data(df)
            if not is_valid:
                st.error(f"⚠️ QA ALERT: Physical inconsistency at {anomalies['Timestamp'].values[0]}s.")
            report = analyzer.get_ai_report("ERR_TIMEOUT")
            st.info(f"🤖 **{report}**")