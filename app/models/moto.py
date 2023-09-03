from ..constants.const import *
from .vehiculo import Vehiculo


class Moto(Vehiculo):
    ''' Class Moto is used to compete. '''

    def __init__(
        self, capacidad: float, cambios: int,
        aceleracion: int, agilidad: int
    ) -> object:
        super().__init__(capacidad, cambios)
        self._aceleracion = aceleracion
        self._agilidad = agilidad

    def get_pos(self) -> dict:
        ''' Function to know the vehicle position '''
        return self._x_pos

    def get_cambios(self) -> dict:
        ''' Function to travel a certain distance '''
        return self._cambios

    def get_capacidad(self) -> dict:
        ''' Function to get the tank capacity '''
        return self._capacidad

    def avanzar(self) -> float:
        ''' Function to advance into the track '''

    def acelerar(self) -> bool:
        ''' Function to travel a certain distance '''
        cambio_perc: float = (self._cambios['actual'] / 10)
        if self.capacidad() <= 0:
            return False
        self._capacidad['actual'] -= KM_GAL_MOTO * cambio_perc

        self._velocidad += (self._aceleracion +
                            self._velocidad * (self._agilidad/10)) * cambio_perc
        return True

    def cambio(self) -> bool:
        if self._cambios['actual'] == self._cambios['limite']:
            return False
        self._cambios['actual'] += 1
        return True

    def frenar(self, distancia) -> bool:
        ''' Function to determine when stop the vehicle '''
        if distancia > 0:
            return False
        self._velocidad = 0
        return True

    def capacidad(self) -> float:
        ''' Returns the left capacity of the vehicle in percentage. '''
        if self._capacidad['actual'] > self._capacidad['total']:
            self._capacidad['actual'] = self._capacidad['total']
        return self._capacidad['actual'] / self._capacidad['total']

    def dar_velocidad(self) -> float:
        ''' Returns the speed of the vehicle. '''
        return self._velocidad * (self._agilidad / 10)

    def __str__(self) -> str:
        view = MOTO_VISTA[-1] if self._es_deportivo else AUTO_VISTA[0]
        return view
