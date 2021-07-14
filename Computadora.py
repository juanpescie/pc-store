class Computer:
    computer_counter = 0

    def __init__(self, name, monitor, keyboard, mouse):
        Computer.computer_counter += 1
        self._id_computer = Computer.computer_counter
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    def __str__(self):
        return f'''
        Computer {self._name}, id: {self._id_computer}
            Components:
                {self._monitor}
                {self._keyboard}
                {self._mouse}
                '''

