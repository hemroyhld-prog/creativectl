import streamlit as st
from creativectl.validators import ScriptValidator
from creativectl.emotional_nlp import EmotionalAnalyzer

st.set_page_config(page_title="Creative Intelligence Console", layout="wide")

st.title("Creative Intelligence Console")
st.caption("Structural & Emotional Analytics Engine")

uploaded_file = st.file_uploader("Upload Script File (.txt)")

if uploaded_file:
    script_text = uploaded_file.read().decode("utf-8")

    validator = ScriptValidator(script_text)
    analyzer = EmotionalAnalyzer(script_text)

    structure = validator.basic_structure_report()
    motifs = validator.count_motifs(["cross", "names", "ledger", "fracture"])
    emotion = analyzer.analyze_sentiment_density()

    # =========================
    # Executive Metrics Row
    # =========================
    st.divider()
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Lines", structure.get("total_lines", 0))
    col2.metric("Scenes Detected", structure.get("scene_count", 0))
    col3.metric("Dialogue Lines", structure.get("dialogue_lines", 0))

    # =========================
    # Structural Health Section
    # =========================
    st.divider()
    st.subheader("Structural Health")

    st.write(structure)

    # =========================
    # Motif Intelligence
    # =========================
    st.divider()
    st.subheader("Motif Distribution")

    st.bar_chart(motifs)

    # =========================
    # Emotional Analysis
    # =========================
    st.divider()
    st.subheader("Emotional Density")

    st.line_chart(emotion)

    st.success("System Status: Operational")
