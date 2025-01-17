import flet as ft
from model.GenderAppModel import GenderAppModel
from util.Observer import Observer


class GenderAppView(Observer):
    def __init__(self, model: GenderAppModel):
        self.model: GenderAppModel = model
        # Registrieren des Observers mit der View
        self.model.add_observer(self)

        # UI-Komponenten
        self.input_textfield = ft.TextField(
            label="",
            multiline=True,
            expand=True,
            fit_parent_size=True,
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
            icon=ft.Icons.SEND,
            # events werden im Controller gemanaged!
        )

        self.reset_button = ft.ElevatedButton(
            text="Zurücksetzen",
            icon=ft.Icons.DELETE,
        )

        self.dropdown = ft.Dropdown(
            disabled=True,
            options=[
                ft.dropdown.Option("Option 1"),
                ft.dropdown.Option("Option 2"),
                ft.dropdown.Option("Option 3"),
            ],
        )

    def build(self) -> ft.Control:
        # Layouting für die Darstellung der View
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("Eingabe", size=20, weight="bold"),
                                    ft.Container(
                                        content=self.input_textfield, expand=4
                                    ),
                                    ft.Container(expand=1),
                                ],
                                expand=True,
                            ),
                            expand=1,
                        ),
                        ft.VerticalDivider(
                            width=1, thickness=1, color="black", opacity=0.5
                        ),
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text("Resultat", size=20, weight="bold"),
                                    ft.Container(
                                        content=self.output_textfield, expand=4
                                    ),
                                    ft.Container(expand=1),
                                ],
                                expand=True,
                            ),
                            expand=1,
                        ),
                    ],
                    expand=True,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            self.submit_button,
                            self.reset_button,
                            ft.Container(expand=True),
                            self.dropdown,
                        ],
                    ),
                    alignment=ft.alignment.bottom_left,
                    expand=False,
                ),
            ],
            expand=True,
        )

    def update(self) -> None:
        # Updatet das Textfeld Output mit dem Input aus dem Model
        self.output_textfield.value = self.model.get_input_text()
        # Updatet das Textfeld Input mit dem Input aus dem Model
        self.input_textfield.value = self.model.get_input_text()
        # (um derzeit Gleichheit zu gewährleisten)

        # Aktualisiert das einzelne Element auf der View
        self.output_textfield.update()
        self.input_textfield.update()
