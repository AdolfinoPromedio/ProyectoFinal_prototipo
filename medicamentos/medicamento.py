#Aquí está la clase medicamento.
class Medicamento:
    #Setter inicial de la clase.
    def __init__(self, nombre, info, precio, UF):
        self.nombre = nombre
        self.info = info
        self.precio = precio
        self.precioUF = self.precio/UF

    #Getters. (En caso de necesitarlos.)
    def getNombre(self):
        return (self.nombre)

    def getInfo(self):
        return (self.info)

    def getPrecio(self):
        return (self.precio)

    def getPrecioUF(self):
        return (self.precioUF)

    #Imprimir todos los datos.
    def getDatos(self):
        print("Nombre: " + self.nombre, "Info: " + self.info, "Precio: " + str(self.precio), "Precio UF: " + str(self.precioUF))
