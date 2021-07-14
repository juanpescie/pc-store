from DispositivoEntrada import DispositivoEntrada

class Keyboard(DispositivoEntrada):
    keyboard_counter = 0
    def __init__(self, marca, tipo_entrada):
        Keyboard.keyboard_counter += 1
        super().__init__(marca, tipo_entrada)
        self._id_keyboard = Keyboard.keyboard_counter

    @property
    def id(self):
        return self._id_keyboard

    def __str__(self):
        return f"KeyBoard, id: {self._id_keyboard}, {super().__str__()}"

