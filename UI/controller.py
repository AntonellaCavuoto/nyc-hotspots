import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_creaGrafo(self, e):
        provider = self._view._ddProvider.value
        distanza = self._view.txt_distanza.value

        if provider is None:
            self._view.create_alert("Inserire un provider")
            return

        if distanza == "":
            self._view.create_alert("Inserire una distanza")
            return

        try:
            distanzaInt = float(distanza)
        except ValueError:
            self._view.create_alert("Inserire un valore numerico per la distanza")
            return

        numNodi, numArchi = self._model.buildGraph(provider, distanzaInt)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato!"))
        self._view.txt_result.controls.append(ft.Text(f"#Vertici: {numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"#Archi: {numArchi}"))

        locations = self._model.getLocations(self._view._ddProvider.value)
        providersDD = []
        for provider in locations:
            providersDD.append(ft.dropdown.Option(provider))
        self._view._ddTarget.options = providersDD
        self._view.update_page()


    def handle_analisiGrafo(self, e):
        nodi, numVicini = self._model.getVicini()
        self._view.txt_result.controls.append(ft.Text(f"VERTICI CON PIU' VICINI:"))
        for n in nodi:
            self._view.txt_result.controls.append(ft.Text(f"{n}, #vicini={numVicini}"))
        self._view.update_page()

    def handle_calcolaPercorso(self, e):
        target = self._view._ddTarget.value
        stringa = self._view.txt_stringa.value

        if target is None:
            self._view.create_alert("Inserire un target")
            return

        if stringa == "":
            self._view.create_alert("Inserire una stringa")
            return

        bestPath, bestScore, nodo = self._model.getBestPath(target, stringa)
        if len(bestPath) != 0:
            self._view.txt_result.controls.append(ft.Text(f"E' stato trovato un percorso da {bestPath[0]} di {bestScore} "
                                                          f"elementi:"))
            for n in bestPath:
                self._view.txt_result.controls.append(ft.Text(f"{n}"))
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(
                ft.Text(f"Non ho trovato un percorso che parte da {nodo}"))
            self._view.update_page()


    def fillDDProvider(self):
        providers = self._model.getProvider()
        providersDD = []
        for provider in providers:
            providersDD.append(ft.dropdown.Option(provider))
        self._view._ddProvider.options = providersDD
        self._view.update_page()


    def fillDDTarget(self):
        locations = self._model.getLocations(self._view._ddProvider.value)
        providersDD = []
        for provider in locations:
            providersDD.append(ft.dropdown.Option(provider))
        self._view._ddTarget.options = providersDD
        self._view.update_page()