import time
import sys
import os


class Out_view:
    ''' Class Out_view is used to animate the output. '''

    def __init__(self) -> object:
        pass

    def plasmar(self, views: list[str]) -> None:
        # The minimal
        for view in views:
            sys.stdout.flush()
            sys.stdout.write(view)
            # Pause of 0.2 secs (by preference)
            # time.sleep(0)
            # Clear the terminal screen
            # os.system('clear')  # For Unix/Linux
            os.system('cls')  # For Windows
