from ..helpers.helper import InputHelper as ih
from ..models.moto import Moto
from ..models.auto import Auto
from ..models.camion import Camion


class Vehiculo_ctrl:
    ''' Class Vehiculo_ctrl is used to CRUD OPS with the model. '''

    def __init__(self) -> None:
        pass

    def crear_moto(self) -> object:
        ''' Function to create a new moto '''
        data: list = []
        prompts: list = [
            'Capacidad (litros)(max:15)', 'Número de cambios', 'Aceleración inicial (m/s^2)',
            'Determine el nivel de agilidad de la moto (1 al 10)'
        ]
        for prompt in prompts:
            data.append(ih.in_int(f'{prompt}: '))
        if data[-1] > 10:
            data[-1] = 10
        return Moto(*data)

    def crear_auto(self) -> object:
        ''' Function to create a new auto '''
        data: list = []
        int_prompts = [
            'Capacidad (en litros)(max:80)', 'Número de cambios'
        ]
        bool_prompts = [
            'Tiene nitro?', 'Es un auto deportivo?'
        ]

        for prompt in int_prompts:
            data.append(ih.in_int(f'{prompt}: '))
        for prompt in bool_prompts:
            data.append(ih.in_bool(f'{prompt}: '))

        return Auto(*data)

    def crear_camion(self) -> object:
        ''' Function to create a new camion '''
        data: list = []
        int_prompts = [
            'Capacidad (en litros)(max:225)', 'Número de cambios',
            'Nivel de resistencia (1 al 10)'
        ]

        for prompt in int_prompts:
            data.append(ih.in_int(f'{prompt}: '))
        data.append(ih.in_bool('Tiene un motor diesel?'))

        return Camion(*data)
