from medicamentos import medicamento as M

class farmacia:

    def __init__(self, nombre, url):
        self.nombre = nombre
        self.url = url

    # Función que recorre las listas de precios, los transforma a UF y luego los almacena en otra lista. Retorna esta lista.
    def precio_to_UF(self, lista_precio, uf_price):
        lista_precio_uf = []  # Lista vacía.
        # Ciclo que recorrerá la lista de precio y calcula el precio en UF, guardandolo en la lista.
        for i in lista_precio:
            lista_precio_uf.append(i / uf_price)  # Se guarda.
        return lista_precio_uf

    # Función que toma las listas de atributos, guarda estos en una estructura y las guarda en una lista.
    def GetObjectList(self, lista_nombre, lista_info, lista_precio, uf_price):
        medicamentos = []  # Lista vacía que guardará los objetos.

        # Ciclo que recorres los atributos de las listas y los guarda en la nueva lista.
        for i in range(0, len(lista_nombre) - 1):
            med = M.Medicamento(lista_nombre[i], lista_info[i], lista_precio[i], uf_price)  # Se crea el objeto medicamento.
            medicamentos.append(med)
        return medicamentos
