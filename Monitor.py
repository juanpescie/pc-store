class Monitor:
    monitor_counter = 0 

    def __init__(self, marca, tamano):
        Monitor.monitor_counter += 1 
        self._id_monitor = Monitor.monitor_counter
        self._marca = marca
        self._tamano = tamano

    @property
    def marca(self):
        return self._marca
    @property
    def tamano(self):
        return self._tamano

    def __str__(self):
        return f"Monitor id:{self._id_monitor}, marca: {self._marca}, tamano: {self._tamano} inches"


