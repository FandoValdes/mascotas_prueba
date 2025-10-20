class Mascota:

    def __init__(self,nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy un {self.tipo} llamado {self.nombre} y tengo {self.edad} años.")

    def cumplir_años(self,años_cumplidos):
        self.edad += años_cumplidos
        if años_cumplidos == 1:
            año_años = "año"
        else:
            año_años= "años"
        return f"¡{self.nombre} ha cumplido {años_cumplidos} {año_años} más! Ahora tiene {self.edad} años."


gallo = Mascota("Chuy","Gallo",5)

gallo.presentarse()
print(gallo.cumplir_años(1))
print(gallo.cumplir_años(2))