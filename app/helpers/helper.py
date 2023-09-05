class InputHelper:
    @staticmethod
    def in_int(prompt: str, in_range: tuple = None):
        while True:
            try:
                user_input = int(input(prompt))
                if in_range is None \
                        or (in_range[0] <= user_input <= in_range[1]):
                    return user_input
                print(
                    f'El valor debe estar entre {in_range[0]} y {in_range[1]} (inclusive).')

            except ValueError:
                print('Por favor, ingresa un número entero válido.')

    @staticmethod
    def in_float(prompt: str, in_range: tuple = None):
        while True:
            try:
                user_input = float(input(prompt))
                if in_range is None \
                        or (in_range[0] <= user_input <= in_range[1]):
                    return user_input
                print(
                    f'El valor debe estar entre {in_range[0]} y {in_range[1]} (inclusive).')
            except ValueError:
                print('Por favor, ingresa un número decimal válido.')

    @staticmethod
    def in_str(prompt: str, options: tuple):
        while True:
            user_input = input(
                prompt + '\n\n|> Ingresa una opción: ').strip().lower()
            if user_input in options:
                return user_input
            print('Por favor, la opción ingresada no una de las definidas.')

    @staticmethod
    def in_bool(prompt):
        while True:
            user_input = input(prompt+'\n[YES|no]: ').strip().lower()
            if user_input in ('yes', 'y', 'si', 's', ''):
                return True
            elif user_input in ('no', 'n'):
                return False
            else:
                print('Por favor, responde "si" ó "no".')
