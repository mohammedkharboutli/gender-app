import re
from typing import Dict, List

class GenderChecker:
    def __init__(self, text: str):
        self.text = text
        self.patterns = {
            'Binnen-I': [r'\b\w+Innen\b'],   # LehrerInnen, SchülerInnen
            'Sternchen': [r'\b\w+\*innen\b'], # Lehrer*innen, Schüler*innen
            'Schrägstrich': [r'\b\w+/innen\b'] # Lehrer/innen, Schüler/innen
        }
        self.formatting = {
            'Binnen-I': lambda word: f"__{word}__",  # Unterstrichen
            'Sternchen': lambda word: f"__{word}__",  # Fett
            'Schrägstrich': lambda word: f"__{word}__"  # Kursiv
        }
    
    def count_gendered_words(self) -> Dict[str, int]:
        word_counts = {}
        for label, patterns in self.patterns.items():
            count = 0
            for pattern in patterns:
                count += len(re.findall(pattern, self.text))
            word_counts[label] = count
        return word_counts
    
    def highlight_gendered_words(self) -> str:
        highlighted_text = self.text
        for label, patterns in self.patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, self.text)
                for match in matches:
                    highlighted_text = highlighted_text.replace(match, self.formatting[label](match))
        return highlighted_text