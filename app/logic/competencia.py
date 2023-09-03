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
        # self._vehiculo_a: Vehiculo = Moto(15, 3, 3, 6) #?
        # self._vehiculo_a: Vehiculo = Moto(12, 5, 8, 4) #? Use it or not? Maybe not
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
            # 'b': vc.nueva_moto, #!!
            # 'c': vc.nueva_moto, #!! To complete
        }
        return self.options[literal]()

    def conducir(self, vehiculo: Vehiculo) -> None:  # ! WIP
        ''' Function to drive the vehicle '''
        # def conducir(self) -> None:
        # ''' Function to update the position of the vehicle by it's attributes '''

        vehiculo: Vehiculo = self._linea_a.get_vehiculo()

        if vehiculo is None:
            return False

        # Turn on the vehicle #
        if vehiculo.get_cambios()['actual'] == 0:
            self.cambio()

        # Capacity is a ratio, full means 1, but slowly decreases cause of ['actual'] is getting close to 0 #
        while vehiculo.capacidad() >= 0:
            self._tiempo += 1
            if vehiculo.acelerar():
                vehiculo.get_pos['final'] += vehiculo.dar_velocidad()

                # vehiculo.cambio() if vehiculo.get_velocidad() <= 0 else None
                # vehiculo.get_pos() += vehiculo.get_velocidad() * \
                #     (vehiculo.get_agilidad() / 10)
            # vehiculo.cambio() if vehiculo.get_velocidad() <= 0 else None
            # vehiculo.get_pos() += vehiculo.get_velocidad() * \
            #     (vehiculo.get_agilidad() / 10)

        # vehiculo.conducir()

        # # Update the vehicle #
        # while
        # self.acelerar()
        # self.cambio() if self._velocidad <= 0 else None

        # self._x_pos += self._velocidad * (self._agilidad / 10)

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
