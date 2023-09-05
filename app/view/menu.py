import pandas as pd

from ..logic.competencia import Competencia
from ..helpers.helper import InputHelper as ih

from .out_view import Out_view


class Menu:
    ''' Class Menu is used to manage the competences. '''

    def __init__(self) -> None:
        self._competencia: Competencia = Competencia()

    def set_up(self) -> None:
        ''' Function to start competition '''
        self.menu()
        data_a: dict = None
        data_b: dict = None
        data_a, data_b = self._competencia.get_data()

        vistas_a: list = data_a['vistas']
        captura_a: int = data_a['registros']

        vistas_b: list = data_b['vistas']
        captura_b: int = data_b['registros']

        self.mostrar_pista(vistas_a, vistas_b)

        self.mostrar_ganador(captura_a, captura_b)

        ver_reportes: bool = ih.in_bool(
            'Mostrar reportes?'
        )

        if ver_reportes:
            reporte_a: pd.DataFrame = None
            reporte_b: pd.DataFrame = None
            reporte_a, reporte_b = self._competencia.get_reportes()
            print(reporte_a)
            print(reporte_b)

        self.salir()

    def menu(self) -> None:
        ''' Function to show the menu '''
        prompt: str = (
            '\n| ¡Bienvenido al simulador de carreras! |'
            '\n| Desarrollado por Over V.              |'
            '\n|                                       |'
            '\n| a ] Iniciar competencia               |'
            '\n| Enter ↵ ] Salir?                      |'
        )
        opcion: str = ih.in_str(prompt, ('a', ''))
        opciones: dict = {
            '': self.salir, 'a': self._competencia.iniciar
        }
        opciones[opcion]()

    def mostrar_ganador(self, captura_a: float, captura_b: float) -> None:
        ''' Function to show the winner '''
        if captura_a < captura_b:
            print(
                f'\n🥇 Felicitaciones corredor A! Tiempo: {captura_a/50} (sec) 🥇'
            )
            print(
                f'\n🥈 Suerte a la próxima corredor B! {captura_b/50} (sec) 🥈\n'
            )
        elif captura_a > captura_b:
            print(
                f'\n🥇 Felicitaciones corredor B! Tiempo: {captura_b/50} (sec) 🥇'
            )
            print(
                f'\n🥈 Suerte a la próxima corredor A! Tiempo: {captura_a/50} (sec) 🥈\n'
            )
        else:
            print(
                f'\n🥇 Soís unos másters... Empate! Tiempos: {captura_b/50} = {captura_a}  🥇'
            )

    def mostrar_pista(self, vistas_a: list[str], vistas_b: list[str]) -> None:
        ''' Function to show the track '''
        visor: Out_view = Out_view()
        visor.plasmar(vistas_a, vistas_b)

    def salir(self) -> None:
        ''' Function to exit '''
        print('Fin de la ejecución\n')
        exit(0)
