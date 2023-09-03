from ..helpers.helper import InputHelper as ih
from ..models.vehiculo import Vehiculo
from ..models.moto import Moto
from ..controller.vehiculo_ctrl import Vehiculo_ctrl as vc


class Competencia:
    ''' Class Competencia is used to compare vehicles and set a winner. '''

    def __init__(self) -> None:
        # self._vehiculo_a: Vehiculo = None
        # self._vehiculo_b: Vehiculo = None
        self._vehiculo_a: Vehiculo = Moto(12, )
        self._vehiculo_b: Vehiculo = Moto()
        self._tiempo: int = 0

    def nuevo_vehiculo(self) -> bool:
        ''' Function to create vehicles '''
        prompt = (
            '| Tipo de vehículo:              |\n'
            '| a) Moto | b) Carro | c) Camion |'
        )
        print(prompt)

        literal: str = ih.in_str(prompt, ('a', 'b', 'c'))
        self.options: dict = {
            'a': vc.nueva_moto,
            # 'b': vc.nueva_moto,
            # 'c': vc.nueva_moto,
        }
        new_vehiculo = self.options[literal]()
        if self._vehiculo_a == None:
            self._vehiculo_a = new_vehiculo
            return True
        if self._vehiculo_b == None:
            self._vehiculo_b = new_vehiculo
            return True
        return False
