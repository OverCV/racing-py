from ..logic.competencia import Competencia
from ..helpers.helper import InputHelper as ih


class Menu:
    ''' Class Menu is used to manage the competences. '''

    def __init__(self) -> None:
        self._competencia: Competencia = Competencia()

    def menu(self) -> None:
        ''' Function to show the menu '''
        prompt: str = (
            '\n| a ] Iniciar competencia |'
            '\n| Enter ↵ ] Salir?        |'
        )
        opcion: str = ih.in_str(prompt, ('a'))
        opciones: dict = {
            '': self.salir, 'a': self._competencia.iniciar
        }
        opciones[opcion]()

    def set_up(self) -> None:
        ''' Function to start competition '''
        self._competencia.iniciar()

    def mostrar_ganador(self) -> None:
        ''' Function to show the winner '''
        pass

    def salir(self) -> None:
        ''' Function to exit '''
        print('Fin de la ejecución')
