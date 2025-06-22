import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_distanza = None
        self.btn_creaGrafo = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("NYC_WIFI_HOTSPOTS", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self._ddProvider = ft.Dropdown(label="Provider")
        self._controller.fillDDProvider()
        self.txt_distanza = ft.TextField(
            label="Distanza",
            width=200,
            hint_text="Inserisci una distanza in km"
        )

        # button for the "hello" reply
        self.btn_creaGrafo = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_creaGrafo)
        self.btn_analisiGrafo = ft.ElevatedButton(text="Analisi grafo", on_click=self._controller.handle_analisiGrafo)

        self.txt_stringa = ft.TextField(
            label="Stringa",
            width=200,
            hint_text="Inserisci una stringa"
        )
        self.btn_calcolaPercorso = ft.ElevatedButton(text="Calcola percorso", on_click=self._controller.handle_calcolaPercorso)

        self._ddTarget = ft.Dropdown(label="Target")

        row2 = ft.Row([self._ddProvider, self.btn_creaGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        row1 = ft.Row([self.txt_distanza, self.btn_analisiGrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        row3 = ft.Row([self.txt_stringa, self.btn_calcolaPercorso],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        row4 = ft.Row([self._ddTarget],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
