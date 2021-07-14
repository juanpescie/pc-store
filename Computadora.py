from Mouse import Mouse
from Monitor import Monitor
from Keyboard import Keyboard

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
        {self._monitor.__str__()}
        {self._keyboard.__str__()}
        {self._mouse.__str__()}
                '''

m1 = Mouse("Genius", "USB")
k1 = Keyboard("Sony", "Inalambrico")
mon1 = Monitor("Sanyo",20)
computer1 = Computer("Razer", mon1, k1, m1)
print(computer1)