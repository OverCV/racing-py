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
        dic_datos: dict = self._competencia.get_pista()
        lista_a: list = dic_datos['a']

        vistas_a: list
        captura_a: int

        vistas_a, captura_a = lista_a
        # vistas_b, captura_b = data['b']

        self.mostrar_pista(vistas_a)

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

    def mostrar_pista(self, vistas) -> None:
        ''' Function to show the track '''
        visor: Out_view = Out_view()
        visor.plasmar(vistas)

    def salir(self) -> None:
        ''' Function to exit '''
        print('Fin de la ejecución')
