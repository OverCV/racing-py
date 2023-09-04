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

        if captura_a < captura_b:
            print(f'\n🥇 Felicitaciones corredor A! Tiempo: {captura_a} 🥇')
            print(f'\n🥈 Suerte a la próxima corredor B! {captura_b} 🥈\n')
        elif captura_a > captura_b:
            print(f'\n🥇 Felicitaciones corredor B! Tiempo: {captura_b} 🥇')
            print(f'\n🥈 Suerte a la próxima corredor A! Tiempo: {captura_a} 🥈\n')
        else:
            print(f'\n🥇 Soís unos másters... Empate! Tiempos: {captura_b} = {captura_a}  🥇')

    def menu(self) -> None:
        ''' Function to show the menu '''
        prompt: str = (
            '\n| a ] Iniciar competencia |'
            '\n| Enter ↵ ] Salir?        |'
        )
        opcion: str = ih.in_str(prompt, ('a', ''))
        opciones: dict = {
            '': self.salir, 'a': self._competencia.iniciar
        }
        opciones[opcion]()

    def mostrar_ganador(self) -> None:
        ''' Function to show the winner '''
        pass

    def mostrar_pista(self, vistas_a: list[str], vistas_b: list[str]) -> None:
        ''' Function to show the track '''
        visor: Out_view = Out_view()
        visor.plasmar(vistas_a, vistas_b)

    def salir(self) -> None:
        ''' Function to exit '''
        print('Fin de la ejecución')
