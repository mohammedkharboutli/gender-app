import flet as ft
from model.GenderAppModel import GenderAppModel
from util.Observer import Observer


class GenderAppView(Observer):
    def __init__(self, page: ft.Page, model: GenderAppModel):
        self.model: GenderAppModel = model
        # Registrieren des Observers mit der View
        self.model.add_observer(self)

        self.header = ft.AppBar(
            leading_width=40,
            title=ft.Text("Gender-App"),
            center_title=True,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        )
    
        # appbar
        page.appbar = self.header

        # UI-Komponenten
        self.input_textfield = ft.TextField(
            label="",
            multiline=True,
            expand=True,
            fit_parent_size=True,
            text_vertical_align=-1,
            autofocus=True,
        )
        self.output_markdown = ft.Markdown(
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            selectable=True,
        )

        self.result_textfield = ft.TextField(
            label="",
            multiline=True,
            expand=True,
            fit_parent_size=True,
            text_vertical_align=-1,
            read_only=True,
        )


        self.description_binnen_i = ft.Text(
            "Binnen-I: LehrerInnen, SchülerInnen, StudentInnen",
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE_600,
        )

        self.description_sternchen = ft.Text(
            "Sternchen: Lehrer*innen, Schüler*innen, Student*innen",
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.GREEN_600,
        )

        self.description_schraegstrich = ft.Text(
            "Schrägstrich: Lehrer/innen, Schüler/innen, Student/innen",
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.ORANGE_600
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
                                    # ft.Container(expand=1),
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
                                    ft.Column(
                                        controls=[self.output_markdown], 
                                        expand=4,
                                        scroll=True,
                                    ),
                                    # ft.Container(expand=1),
                                ],
                                expand=True,
                            ),
                            expand=1,
                        ),
                    ],
                    expand=7
                ),
                ft.Divider(),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    self.description_binnen_i,
                                    self.description_sternchen,
                                    self.description_schraegstrich,
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
                                    ft.Container(
                                        content=self.result_textfield, expand=2
                                    ),
                                    ft.Row(
                                        controls=[
                                            self.submit_button,
                                            ft.Container(expand=1), # Placeholder
                                            self.reset_button,
                                        ],
                                        expand=1,
                                    ),
                                ],
                                expand=True,
                            ),
                            expand=1,
                        ),
                    ],
                    expand=1
                ),
            ],
            expand=True,
        )

    def update(self) -> None:
        # Updatet das Textfeld Input mit dem Input aus dem Model
        self.input_textfield.value = self.model.get_input_text()
        # Updatet das Textfeld Output mit dem Input aus dem Model
        self.output_markdown.value = self.model.get_output_text()
        # Updatet das Textfeld Result mit dem Input aus dem Model
        self.result_textfield.value = self.model.get_result_text()
        # Aktualisiert das einzelne Element auf der View
        self.input_textfield.update()
        self.output_markdown.update()
        self.result_textfield.update()
