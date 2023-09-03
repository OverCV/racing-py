from abc import ABC, abstractmethod, abstractproperty


class Vehiculo(ABC):
    ''' Class Vehiculo is used to model different vehicles. '''

    def __init__(
        self, capacidad: float, cambios: int
    ) -> object:
        self._x_pos: int = 0
        self._velocidad: float = 0
        self._cambios: dict = {'actual': 0, 'limite': cambios}
        self._capacidad: dict = {'actual': capacidad, 'total': capacidad}

    @abstractmethod
    def acelerar(self) -> bool:
        ''' Function to travel a certain distance '''
        pass

    @abstractmethod
    def cambio(self) -> bool:
        pass

    @abstractmethod
    def frenar(self, distancia) -> bool:
        ''' Function to stop if already has crossed the line '''
        pass

    @abstractmethod
    def capacidad(self) -> float:
        ''' Returns the left capacity of the vehicle in percentage. '''
        pass

    @abstractmethod
    def dar_velocidad(self) -> float:
        ''' Returns the speed of the vehicle. '''
        pass
