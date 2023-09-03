from ..constants.const import *
from .vehiculo import Vehiculo


class Moto(Vehiculo):
    ''' Class Moto is used to compete. '''

    def __init__(
        self, velocidad: float, capacidad: float, cambios: int,
        aceleracion: int, agilidad: int
    ) -> object:
        super().__init__(velocidad, capacidad, cambios)
        self._aceleracion = aceleracion
        self._agilidad = agilidad

    def acelerar(self) -> bool:
        ''' Function to travel a certain distance '''
        if self.dar_capacidad() <= 0:
            return False
        self._capacidad -= KM_DIESEL * (self._cambios['actual'] / 10)
        self._velocidad += self._aceleracion
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

    def dar_capacidad(self) -> float:
        ''' Returns the capacity of the vehicle. '''
        return self._capacidad

    def dar_velocidad(self) -> float:
        ''' Returns the speed of the vehicle. '''
        return self._velocidad * (self._agilidad / 10)

    def __str__(self) -> str:
        view = MOTO_VISTA[-1] if self._es_deportivo else AUTO_VISTA[0]
        return view
