class Usuario:
    def __init__(self):
        pass

    def create(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        return f"Usuario creado: Nombre: {self.nombre}, Edad: {self.edad}"

    def view(self, x, y):
        self.x = x
        self.y = y

        return x + y