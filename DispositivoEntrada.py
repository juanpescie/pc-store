class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self._marca
        
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    def setMarca(self, nuevaMarca):
        self._marca = nuevaMarca
    def setTipoEntrada(self, nuevoTipo):
        self._tipo_entrada = nuevoTipo

    def __str__(self):
        return f"marca: {self._marca}, entrada: {self._tipo_entrada}"

