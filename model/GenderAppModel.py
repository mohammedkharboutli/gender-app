from util.Observable import Observable


class GenderAppModel(Observable):
    def __init__(self):
        super().__init__()
        self.input_text: str = ""

    def set_input_text(self, text: str) -> None:
        # Setzt den aktuellen Text
        self.input_text: str = text
        # Benachrichte alle Abonnenten des Observers
        self.notify_observers()

    def get_input_text(self) -> str:
        # Gibt den aktuellen Text zurück
        return self.input_text
