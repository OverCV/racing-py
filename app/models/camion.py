from ..constants.const import *
from .vehiculo import Vehiculo


class Camion(Vehiculo):
    ''' Class Camion is used to compete. '''

    def __init__(
        self, capacidad: float, cambios: int,
        resistencia: int, es_diesel: bool
    ) -> object:
        super().__init__(capacidad, cambios)
        self._resistencia: int = resistencia
        self._es_diesel: int = es_diesel
        self._img: str = ''

    def get_pos(self) -> float:
        ''' Function to know the vehicle position '''
        return self._x_pos

    def set_pos(self, pos: float) -> float:
        ''' Function to travel a certain distance '''
        self._x_pos = pos

    def get_cambios(self) -> dict:
        ''' Function to travel a certain distance '''
        return self._cambios

    def get_capacidad(self) -> dict:
        ''' Function to get the tank capacity '''
        return self._capacidad

    def acelerar(self) -> bool:
        ''' Function to travel a certain distance '''
        cambio_perc: float = (self._cambios['actual'] / 50)
        if self.capacidad() <= 0:
            return False
        tipo_combustible: float = KM_DIESEL_CAMION if self._es_diesel else KM_GAL_CARRO
        self._capacidad['actual'] -= tipo_combustible * cambio_perc

        self._velocidad += (self._es_diesel * cambio_perc) + \
            (self._cambios['limite'] * self._es_diesel) * 0.1
        return True

    def cambio(self) -> bool:
        ''' Function to change the gear '''
        if self._cambios['actual'] == self._cambios['limite']:
            return False
        self._cambios['actual'] += 1
        return True

    def frenar(self, distancia) -> bool:
        ''' Function to determine when stop the vehicle '''
        if distancia <= 0:
            return True
        self._velocidad = 0
        return False

    def capacidad(self) -> float:
        ''' Returns the left capacity of the vehicle in percentage. '''
        if self._capacidad['actual'] > self._capacidad['total']:
            self._capacidad['actual'] = self._capacidad['total']
        return self._capacidad['actual'] / self._capacidad['total']

    def dar_velocidad(self) -> float:
        ''' Returns the speed of the vehicle. '''
        return self._velocidad + (self._cambios['limite'] * self._es_diesel) * 0.01 + \
            (self._resistencia * 0.01)

    def __str__(self) -> str:
        if self._img == '':
            self._img = get_camion()
        return self._img
