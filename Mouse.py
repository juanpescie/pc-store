from DispositivoEntrada import DispositivoEntrada

class Mouse(DispositivoEntrada):
    mouse_counter = 0
    def __init__(self, marca, tipo_entrada):
        Mouse.mouse_counter += 1 
        super().__init__(marca, tipo_entrada)
        self._id_mouse = Mouse.mouse_counter

    @property
    def id(self):
        return self._id_mouse

    def __str__(self):
        return f"Mouse id: {self._id_mouse}, {super().__str__()}"

