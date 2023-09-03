import math

from ..helpers.helper import InputHelper as ih
from ..models.vehiculo import Vehiculo
from ..controller.vehiculo_ctrl import Vehiculo_ctrl
from .linea import Linea


class Competencia:
    ''' Class Competencia is used to compare vehicles and set a winner. '''

    def __init__(self) -> None:
        self._historicos: dict = {'a': None, 'b': None}
        self._linea_a: Linea
        self._linea_b: Linea
        self._pista = {'a': [], 'b': []}

    def iniciar(self) -> None:
        ''' Function that returns the winner vehicle  '''
        self.nueva_pista()
        vistas_a, captura_a = self.conducir(self._linea_a)
        # vistas_b, captura_b = self.conducir(self._linea_b)

        # !! Incorrect btw, use one below
        self._pista['a'] = (vistas_a, captura_a)
        # self._pista['a'], self._pista['b'] = (vistas_a, captura_a), (vistas_b, captura_b)

    def get_pista(self) -> dict[list[str], list[str]]:
        ''' Function to get the track '''
        return self._pista

    def conducir(self, linea: Linea) -> tuple[list[str], int]:
        '''
        Function to drive the vehicle, it's planned to function as:
        If the vehicle is stopped, it will turn on
        When turned on, will accelerate
        Acceleration will increase the speed
        Speed will increase the position and decreases the capacity
        if capacity overcomes in a ratio the number of changes that the vehicle has, it will change to the next gear.
        '''

        tiempo: int = 0
        vehiculo: Vehiculo = linea.get_vehiculo()
        meta: int = linea.get_largo()
        vistas: list['str'] = []

        if vehiculo is None:
            return False

        # Turn on the vehicle #
        if vehiculo.get_cambios()['actual'] == 0:
            vehiculo.cambio()

        fase_continua = vehiculo.get_cambios()['limite']
        fase_discreta = vehiculo.get_cambios()['limite']

        # Capacity is a ratio, full means 1, but slowly decreases cause of ['actual'] is getting close to 0 #
        while vehiculo.capacidad() >= 0:
            # For devs: Imagine a bar that decreases starting from 3 to 0 by continous scalar, this cursor has a copy, this one behind is discrete and gets substracted every time it's difference is bigger than 1 the discrete one gets substracted by 1, that happens until foreground bar is 0 and the difference is 0, it mustn't change anymore, is over #
            desfase_a: int = fase_discreta - \
                (fase_continua * vehiculo.capacidad())

            if desfase_a > 1:
                vehiculo.cambio()
                fase_discreta -= 1

            # If the vehicle has crossed the finish line, should stop #
            distancia: float = meta - vehiculo.get_pos()
            if vehiculo.frenar(distancia):
                captura: int = tiempo
                break

            # Save a preview of where it was the vehicle to print it and update it's position #
            if vehiculo.acelerar():
                new_pos: float = self.deininir_pos(vehiculo, tiempo)

                vehiculo.set_pos(new_pos)
                vista = linea.locar_vehiculo(new_pos)
                vistas.append(vista)

            # Final step, next iteration #
            tiempo += 1

        return vistas, captura

    def deininir_pos(self, vehiculo: Vehiculo, tiempo: int) -> float:
        ''' Function to determine the position of the vehicle '''
        velocidad: float = vehiculo.dar_velocidad()
        x_pos: float = velocidad * tiempo
        return x_pos

    def nueva_pista(self) -> None:
        ''' Function to create a new track '''
        largo: int = ih.in_int('\nLargo de la pista (metros): ')
        print('\nCREACIÓN COMPETIDOR A: ')
        self._linea_a: Linea = Linea(largo, self.nuevo_vehiculo())
        print('\nCREACIÓN COMPETIDOR B: ')
        self._linea_b: Linea = Linea(largo, self.nuevo_vehiculo())

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
            # 'b': vc.nueva_moto, #!!
            # 'c': vc.nueva_moto, #!! To complete
        }
        return self.options[literal]()
