import flet as ft

from controller.GenderAppController import GenderAppController
from model.GenderAppModel import GenderAppModel
from view.GenderAppView import GenderAppView

def main(page: ft.Page) -> None:
    page.theme_mode = "light"
    page.title = "Gender-App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # light mode

    # Initialisiere MVC-Komponenten
    model = GenderAppModel()
    view = GenderAppView(model)
    controller = GenderAppController(model, view)

    # Füge die View-Komponenten zur Seite hinzu
    page.add(view.build())

# Starte die Flet-App
ft.app(target=main)