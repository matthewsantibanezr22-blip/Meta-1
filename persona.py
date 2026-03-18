class Alumno:
    def __init__(self, nombre, edad, anio_nacimiento):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento
        self.edad = edad

    def calcular_edad(self, anio_nacimiento, anio_actual):
        self.edad = anio_actual - anio_nacimiento
        return self.edad


