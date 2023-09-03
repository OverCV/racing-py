from ..helpers.helper import InputHelper as ih
from ..models.vehiculo import Vehiculo
from ..models.moto import Moto
from ..controller.vehiculo_ctrl import Vehiculo_ctrl
from .linea import Linea


class Competencia:
    ''' Class Competencia is used to compare vehicles and set a winner. '''

    def __init__(self) -> None:
        # self._vehiculo_a: Vehiculo = None
        # self._vehiculo_b: Vehiculo = None
        # self._vehiculo_a: Vehiculo = Moto(15, 3, 3, 6)
        # self._vehiculo_a: Vehiculo = Moto(12, 5, 8, 4)
        self._tiempo: int = 0
        self._linea_a: Linea
        self._linea_b: Linea

    def nuevo_vehiculo(self) -> Vehiculo:
        ''' Function to create vehicles '''
        _vehiculo_ctrl: Vehiculo_ctrl = Vehiculo_ctrl()
        prompt = (
            '\n| Tipo de vehículo:              |'
            '\n| a) Moto | b) Carro | c) Camion |'
        )

        literal: str = ih.in_str(prompt, ('a', 'b', 'c'))
        self.options: dict = {
            'a': _vehiculo_ctrl.crear_moto,
            # 'b': vc.nueva_moto,
            # 'c': vc.nueva_moto,
        }
        return self.options[literal]()

    def nueva_pista(self) -> None:
        ''' Function to create a new track '''
        largo: int = ih.in_int('\nLargo de la pista (metros): ')
        print('\nCREACIÓN COMPETIDOR A: ')
        self._linea_a: Linea = Linea(largo, self.nuevo_vehiculo())
        print('\nCREACIÓN COMPETIDOR B: ')
        self._linea_b: Linea = Linea(largo, self.nuevo_vehiculo())

    def iniciar(self) -> Vehiculo:
        ''' Function that returns the winner vehicle  '''
        self.nueva_pista()
