import streamlit as st
from validators import ScriptValidator
from emotional_nlp import EmotionalAnalyzer

st.title("Creative Infrastructure Dashboard")

uploaded_file = st.file_uploader("Upload Script File")

if uploaded_file:
    script_text = uploaded_file.read().decode("utf-8")

    validator = ScriptValidator(script_text)
    analyzer = EmotionalAnalyzer(script_text)

    structure = validator.basic_structure_report()
    motifs = validator.count_motifs(["cross", "names", "ledger", "fracture"])
    emotion = analyzer.analyze_sentiment_density()

    st.header("Structural Health")
    st.json(structure)

    st.header("Motif Distribution")
    st.json(motifs)

    st.header("Emotional Analysis")
    st.json(emotion)

    st.success("Production Build Active")