

from util.Observable import Observable


class GenderAppModel(Observable):
    def __init__(self):
        super().__init__()
        self.input_text: str = ""

    def set_input(self, text: str) -> None:
        """
        Aktualisiert den Text und benachrichtigt alle Observer.
        """
        self.input_text: str = text
        print("GenderAppModel.set_input:", text)
        self.notify_observers()

    def get_input(self) -> str:
        """
        Gibt den aktuellen Text zurück.
        """
        return self.input_text