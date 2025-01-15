import flet as ft
from controller import GenderAppController
from model.GenderAppModel import GenderAppModel
from util.Observer import Observer

class GenderAppView(Observer):
    def __init__(self, model):
        self.model = model
        self.model.add_observer(self)  # Register the view as an observer
        self.controller = None  # Placeholder for the controller

        # UI-Komponenten
        self.input_textfield = ft.TextField(
            label="",
            multiline=True,
            expand=True,  # Ensures the TextField fills the entire container
            fit_parent_size=True,  # Ensures the TextField fills the entire container
            # min_lines=15,
            text_vertical_align=-1,
            # input_filter=ft.InputFilter(regex_string=r"^[a-zA-Z\s\n\.!?\-\_\|]*$", allow=True, replacement_string=""),
            autofocus=True,
        )
        self.output_textfield = ft.TextField(
            label="",
            multiline=True,
            expand=True,
            fit_parent_size=True, 
            text_vertical_align=-1,
            read_only=True,

        )
        self.submit_button = ft.ElevatedButton(
            text="Abschicken",
            icon=ft.Icons.SEND,  # Korrekte Icons-Nutzung
            on_click=self.on_submit_click
        )

    def set_controller(self, controller):
        """
        Verknüpft die View mit einem Controller.
        """
        self.controller = controller

    def build(self):
        """
        Erstellt das Layout der View.
        """
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("Eingabe", size=20, weight="bold"),
                                    ft.Container(
                                        content=self.input_textfield,
                                        expand=4  # Ensures the TextField fills the full height of the container
                                    ),
                                    ft.Container(
                                        expand=1  # Ensures the container fills the remaining space
                                    ),
                                ],
                                expand=True  # Ensures the column stretches fully
                            ),
                            expand=1,  # Left container expands fully
                        ),
                        ft.VerticalDivider(  # Trennlinie zwischen den Spalten
                            width=1,
                            thickness=1,
                            color="black",
                            opacity=0.5
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("Resultat", size=20, weight="bold"),
                                    ft.Container(
                                        content=self.output_textfield,
                                        expand=4  # Ensures the TextField fills the full height of the container
                                    ),
                                    ft.Container(
                                        expand=1  # Ensures the container fills the remaining space
                                    ),
                                ],
                                expand=True  # Ensures the column stretches fully
                            ),
                            expand=1,  # Right container expands fully
                        )
                    ],
                    expand=True
                ),
                ft.Container(
                    content=self.submit_button,
                    alignment=ft.alignment.bottom_left,  # Align button to the bottom left
                    expand=False  # No need to expand this container
                )
            ],
            expand=True  # The entire column stretches to fill the space
        )

    def on_text_change(self, e):
        """
        Meldet Textänderungen an den Controller.
        """
        if self.controller:
            self.controller.handle_text_change(e.control.value)

    def on_submit_click(self, e):
        """
        Meldet das Klicken des Buttons an den Controller.
        """
        if self.controller:
            self.controller.handle_text_change(self.input_textfield.value)

    def update(self):
        """
        Reagiert auf Änderungen im Model und aktualisiert das Ergebnis.
        """
        self.output_textfield.value = self.model.get_input()
        self.output_textfield.update()