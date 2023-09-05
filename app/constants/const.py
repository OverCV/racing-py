import random

AVG_CAP_MOTO: float = 15  # Gallons
AVG_CAP_CARRO: float = 80  # Gallons
AVG_CAP_CAMION: float = 225  # Gallons

KM_GAL_MOTO: float = 0.03
KM_GAL_CARRO: float = 0.08
KM_GAL_CAMION: float = 1/7
KM_DIESEL_CAMION: float = 2/7

AUTO_VISTA = ['🚗', '🚙', '🚕', '🚓', '🏎️']
CAMION_VISTA = ['🚑', '🚐', '🚚', '🚛', '🚒']
MOTO_VISTA = ['🛵', '🏍️']

# Maybe 🏍️💨? Haha.

GRID_IDEA = '''
[ Vehicle I: ]
[_______________________________________________________🚗]
[ Vehicle II: ]
[_______________________________________________________🏍️]
'''


def get_auto(es_deportivo: bool = False) -> str:
    if es_deportivo:
        return AUTO_VISTA[-1]
    return AUTO_VISTA[random.randint(0, len(AUTO_VISTA) - 2)]


def get_camion() -> str:
    return CAMION_VISTA[random.randint(0, len(CAMION_VISTA) - 1)]


def get_moto(es_agil: bool = False) -> str:
    if es_agil:
        return MOTO_VISTA[-1]
    return MOTO_VISTA[0]
