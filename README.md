# SmartCAN Analyzer: AI-Powered ADAS Validation Tool 🚗🤖

## 🎯 The Problem & The "Why"
In modern automotive engineering, validating **ADAS (Advanced Driver Assistance Systems)** involves analyzing massive amounts of CAN bus data. Manual diagnostic is time-consuming and prone to human error. 

**SmartCAN Analyzer** was developed to bridge the gap between raw telemetry and expert knowledge. By using **Artificial Intelligence**, it automates the identification of anomalies and provides immediate technical recommendations based on engineering manuals, reducing diagnostic time and increasing safety reliability.

---

## 🛠️ System Architecture
The project follows a modular pipeline designed for scalability:
1. **Data Acquisition**: Simulates CAN bus messages (via COM API logic).
2. **QA Validation Layer**: A physical constraint filter that catches "impossible" sensor data before it reaches the AI.
3. **AI Reasoning (RAG)**: Integrates technical knowledge bases with LLMs to interpret error signatures.
4. **Interactive GUI**: A Streamlit dashboard for real-time visualization.



---

## 🚀 Key Features
- **Deterministic QA**: Custom Python logic to validate signal integrity (e.g., negative distance detection).
- **Context-Aware Diagnostics**: Instead of generic errors, the AI points to specific hardware components like "harness connectors" or "radar alignment".
- **Clean Code (OOP)**: Fully developed using Object-Oriented Programming for better maintenance.

---

## 📈 Dashboard Preview
The dashboard provides a clear view of:
- **Real-time Telemetry**: Highlighting corrupted data in red.
- **System Health Metrics**: KPI tracking for ADAS reliability.
- **AI Verdicts**: Actionable insights for validation engineers.

---

## 💻 Technical Stack
- **Language**: Python 3.12 (Standard in AI Engineering)
- **Frameworks**: Pandas (Data), Streamlit (UI), Google Gemini (Intelligence)
- **Version Control**: Professional Git workflow with `.gitignore` optimization.

---

## ⚙️ How to Run
1. Clone the repo: `git clone https://github.com/luciano-lins/SmartCAN-ADAS-AI.git`
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`