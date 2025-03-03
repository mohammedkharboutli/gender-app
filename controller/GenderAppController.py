import flet as ft

from model.GenderAppModel import GenderAppModel
from view.GenderAppView import GenderAppView
from model.GenderChecker import GenderChecker


class GenderAppController:
    def __init__(self, model: GenderAppModel, view: GenderAppView):
        self.model: GenderAppModel = model
        self.view: GenderAppView = view

        # Event Management für View:
        # On-Click-Event für den Abschicken-Button registrieren
        self.view.submit_button.on_click = self.on_click_submit_button
        self.view.reset_button.on_click = self.on_click_reset_button

    def on_click_submit_button(self, e: ft.ControlEvent) -> None:
        # Submit-Button wird geklickt
        # InputText aus Textfield wird ausgelesen
        input_text = self.view.input_textfield.value
        # InputText wird dem Model übergeben
        self.model.set_input_text(input_text)

        checked_text = GenderChecker(input_text)
        result_text = str(checked_text.count_gendered_words())
        self.model.set_result_text(result_text)

        highlighted_text = checked_text.highlight_gendered_words()
        print(highlighted_text)
        self.model.set_output_text(highlighted_text)

    def on_click_reset_button(self, e: ft.ControlEvent) -> None:
        # Reset-Button wird geklickt
        # Model wird zurückgesetzt
        reset_text = ""
        self.model.set_input_text(reset_text)
        self.model.set_output_text(reset_text)
        self.model.set_result_text(reset_text)
    


