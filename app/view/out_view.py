import time
import sys
import os


class Out_view:
    ''' Class Out_view is used to animate the output. '''

    def __init__(self) -> object:
        pass

    def plasmar(self, views_a: list[str], views_b: list[str]) -> None:
        print('\n')
        for view_a, view_b in zip(views_a, views_b):
            sys.stdout.flush()
            os.system('cls')  # For Windows
            sys.stdout.write(view_a+'\n')
            sys.stdout.write(view_b+'\n')
            # time.sleep(0)
