def impulso(cambios):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Obtén el valor actual y el límite de cambios
            if callable(cambios):
                cambios_dict = cambios(self)
            else:
                cambios_dict = cambios

            actual = cambios_dict.get('actual', 0)
            limite = cambios_dict.get('limite', 0)

            # Aplica la lógica del decorador
            result = func(self, *args, **kwargs)
            if actual > limite/2:
                return result * 2
            return result

        return wrapper

    return decorator
