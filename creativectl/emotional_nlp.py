import spacy

class EmotionalAnalyzer:
    _nlp = None

    @classmethod
def get_model(cls):
    if cls._nlp is None:
        cls._nlp = spacy.load("en_core_web_sm")
    return cls._nlp

    def __init__(self, script_text):
        self.script_text = script_text
        self.doc = self.get_model()(script_text)

    def analyze_sentiment_density(self):
        emotional_words = [
            token.text for token in self.doc
            if token.pos_ in ["ADJ", "ADV"]
        ]

        return {
            "emotional_word_count": len(emotional_words),
            "sample": emotional_words[:15]
        }

    def dialogue_density(self):
        lines = self.script_text.split("\n")
        dialogue_lines = [line for line in lines if '"' in line]

        return {
            "dialogue_lines": len(dialogue_lines),
            "total_lines": len(lines)
        }
