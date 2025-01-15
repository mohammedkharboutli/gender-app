import flet as ft

from model.GenderAppModel import GenderAppModel
from view.GenderAppView import GenderAppView


class GenderAppController:
    def __init__(self, model, view):
        self.model: GenderAppModel = model
        self.view: GenderAppView = view
        self.view.set_controller(self)  # Verknüpfe den Controller mit der View

    def handle_text_change(self, text: str) -> None:
        """
        Aktualisiert das Model, wenn sich der Text ändert.
        """
        print("GenderAppController.handle_text_change:", text)
        self.model.set_input(text)