from ..helpers.helper import InputHelper as ih
from ..models.moto import Moto
# from ..models.auto import auto
# from ..models.camion import camion


class Vehiculo_ctrl:
    ''' Class Vehiculo_ctrl is used to CRUD OPS with the model. '''

    def __init__(self) -> None:
        pass

    def crear_moto(self) -> object:
        ''' Function to create a new moto '''
        data: list = []
        prompts: list = [
            'Capacidad (litros)', 'Número de cambios', 'Aceleración inicial (m/s^2)',
            'Determine el nivel de agilidad de la moto (1 al 10)'
        ]
        for prompt in prompts:
            data.append(ih.in_int(f'{prompt}: '))
        if data[-1] > 10:
            data[-1] = 10
        return Moto(*data)

    # def crear_auto(self) -> object:
    #     ''' Function to create a new moto '''
    #     data: list = []
    #     prompts = ['Capacidad (en litros)', 'Número de cambios',
    #                'Aceleración inicial (m/s^2)',
    #                'Determine el nivel de agilidad de la moto (1 al 10)']

    #     for prompt in prompts:
    #         data.append(ih.in_int(prompt))
    #     if data[-1] > 10:
    #         data[-1] = 10
    #     self.moto: Moto = Moto(*data)

    # def crear_camiono(self) -> object:
    #     ''' Function to create a new moto '''
    #     data: list = []
    #     prompts = ['Capacidad (en litros)', 'Número de cambios',
    #                'Aceleración inicial (m/s^2)',
    #                'Determine el nivel de agilidad de la moto (1 al 10)']

    #     for prompt in prompts:
    #         data.append(ih.in_int(prompt))
    #     if data[-1] > 10:
    #         data[-1] = 10
    #     self.moto: Moto = Moto(*data)
