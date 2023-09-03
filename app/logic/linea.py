from ..models.vehiculo import Vehiculo


class Linea:
    ''' Class Pista is used to set a scenario for vehicles to compete. '''

    def __init__(self, largo: int, vehiculo: Vehiculo = None) -> None:
        self._vehiculo: Vehiculo = vehiculo
        self._largo: int = largo
        self._pista: str = ''

    def set_pista(self) -> None:
        ''' Function to set the track '''
        self._pista = self.get_pista()

    def get_vehiculo(self) -> Vehiculo:
        ''' Function to return the object '''
        return self._vehiculo

    def get_largo(self) -> int:
        ''' Function to get the pista size '''
        return self._largo

    def get_pista(self) -> str:
        ''' Function to get the pista size '''
        return f'[{"_" * self._largo}]'

    def puede_locar(self, pos: float) -> bool:
        ''' Function to determine if the position the vehicle into the track is valid '''
        if self._pista == '':
            return False
        if pos >= len(self._pista) - 1:
            return False
        return True

    def locar_vehiculo(self, pos: float) -> str:
        ''' Function to set the vehicle into the track '''
        if not self.puede_locar(pos):
            return '[ 🏆🏁 Finished 🏁🏆 ]'
        vista_pista = self._pista[int(-pos)] \
            .replace(' ', self.vehiculo.__str__())
        return vista_pista

        # self._pista = self._pista[:int(pos)] + self._pista[int(pos):].replace(' ', self._vehicle_a.get_vista())
