import flet as ft

from controller.GenderAppController import GenderAppController
from model.GenderAppModel import GenderAppModel
from view.GenderAppView import GenderAppView


def main(page: ft.Page) -> None:
    page.theme_mode = "light"
    page.title = "Gender-App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Initialisiere MVC-Komponenten
    model = GenderAppModel()
    view = GenderAppView(page, model)
    controller = GenderAppController(model, view)

    # Füge die View-Komponenten zur Seite hinzu
    page.add(controller.view.build())


# Starte die Flet-App
ft.app(target=main)
