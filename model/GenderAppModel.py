from model.GenderChecker import GenderChecker
from util.Observable import Observable


class GenderAppModel(Observable):
    def __init__(self):
        super().__init__()
        self.input_text: str = ""
        self.result_text: str = ""
        self.output_text: str = ""

    def set_input_text(self, text: str) -> None:
        # Setzt den aktuellen Text
        self.input_text: str = text
        # Benachrichte alle Abonnenten des Observers
        self.notify_observers()

    def get_input_text(self) -> str:
        # Gibt den aktuellen Text zurück
        return self.input_text
 

    def set_result_text(self, text: str) -> None:
        # Erstellt ein GenderChecker-Objekt mit dem aktuellen Text
        checked_text = GenderChecker(text)
        # Zählt die gendered words
        result_text = str(checked_text.count_gendered_words())
        # Setzt den aktuellen Text
        self.result_text: str = result_text
        # Benachrichte alle Abonnenten des Observers
        self.notify_observers()

    def get_result_text(self) -> str:
        # Gibt den aktuellen Text zurück
        return self.result_text
    
    def set_output_text(self, text: str) -> None:
        # Erstellt ein GenderChecker-Objekt mit dem aktuellen Text
        checked_text = GenderChecker(text) 
        # Highlighted den Text
        highlighted_text = checked_text.highlight_gendered_words()
        # Setzt den aktuellen Text
        self.output_text: str = highlighted_text
        # Benachrichte alle Abonnenten des Observers
        self.notify_observers()

    def get_output_text(self) -> str:
        # Gibt den aktuellen Text zurück
        return self.output_text