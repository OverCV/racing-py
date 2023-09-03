import random

KM_GAL = 35
KM_DIESEL = 40

AUTO_VISTA = ['🚗', '🚙', '🚕', '🚓', '🏎️']
CAMION_VISTA = ['🚑', '🚐', '🚚', '🚛', '🚒']
MOTO_VISTA = ['🛵', '🏍️']

GRID = '''
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

def get_moto(es_deportivo: bool = False) -> str:
    if es_deportivo:
        return MOTO_VISTA[-1]
    return MOTO_VISTA[0]
