from ..models.vehiculo import Vehiculo


class Linea:
    ''' Class Pista is used to set a scenario for vehicles to compete. '''

    def __init__(self, largo: int, vehiculo: Vehiculo = None) -> None:
        self._vehiculo: Vehiculo = vehiculo
        self._largo: int = largo
        self._pista: str = ''

    def init_pista(self) -> None:
        ''' Function to set the track '''
        self._pista = f'[🏁{self.get_pista()}]'

    def get_vehiculo(self) -> Vehiculo:
        ''' Function to return the object '''
        return self._vehiculo

    def get_largo(self) -> int:
        ''' Function to get the pista size '''
        return self._largo

    def get_pista(self) -> str:
        ''' Function to get the pista size '''
        return '_' * self._largo

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

        return self._pista[:-int(pos+3)] + self._vehiculo.__str__() + self._pista[-int(pos+2):]
        # self._pista[-int(pos + 2)] \
        # .replace(' ', )
