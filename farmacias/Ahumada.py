from bs4 import BeautifulSoup
import requests
from medicamentos import medicamento as M

#Paquete de funciones para la farmacia Ahumada.

#Función que va avanzando de página. Retorna el link de la página siguiente.
def Get_NextPage(website):
    response = requests.get(website) #Obtiene los datos de la página.
    soup = BeautifulSoup(response.content, 'html.parser') #Los datos se pasan a texto.
    a_next_page = soup.find("a", {"class": "action next"}) #Se busca la parte donde está el link de la siguiente página.
    if (a_next_page is None):
        #Si se encuentra en la última página, retorna un 0.
        return 0
    else:
        return a_next_page.get('href') #Retorna el link.

#Función que obtiene los datos del producto buscado (medicamento) y devuelve listas con todos los atributos encontrados.
def GetData(medicamento):
    website = 'https://www.farmaciasahumada.cl/catalogsearch/result/index/?p=' + str(1) + "&q=" + medicamento #Link de la página.

    #Se instancian listas vacías que se irán llenando.
    lista_nombre = list()
    lista_info = list()
    lista_precio = list()
    lista_farmacia = list()

    #Ciclo que irá recorriendo las páginas de la farmacia de los productos encontrados.
    while (website != 0):
        response = requests.get(website) #Se obtienen los datos de la página.
        soup = BeautifulSoup(response.content, 'html.parser') #Se pasa a texto.

        #Se buscan los datos correspondientes.
        nombre = soup.find_all('p', {"class": 'product-brand-name truncate'})
        info = soup.find_all('a', {"class": 'product-item-link'})
        precio = soup.find_all('span', {"class": 'price'})

        #ciclo que recorre los datos encontrados y los va guardando en listas.
        for k in range(len(nombre)):
            lista_nombre.append(nombre[k].getText()) #Nombre.
            lista_info.append(info[k].getText()) #Descripción.
            lista_precio.append(precio[k].getText()) #Precio
            lista_farmacia.append('Ahumada') #Farmacia.

        #Se pasa a la siguiente página.
        website = Get_NextPage(website)

    lista_info = [" ".join(s.split()) for s in lista_info] #Se eliminan especios innecesarios.

    return lista_nombre, lista_info, lista_precio, lista_farmacia #Se retornan las listas.

#Función que recorre las listas de precios, los transforma a UF y luego los almacena en otra lista. Retorna esta lista.
def precio_to_UF(lista_precio, uf_price): #Precio como str ($1.690)
    lista_precio = [s.replace("$", "") for s in lista_precio] #Se reemplaza el signo peso por nada.
    lista_precio = [s.replace(".", "") for s in lista_precio] #Se reemplaza los puntos por nada.
    lista_precio = [int(i) for i in lista_precio] #Se convierte a número los precios.

    lista_precio_uf = [] #Lista vacía donde irán los precios en UF.

    #Ciclo que recorre la lista de precios, y que guarda los datos en UF en la nueva lista.
    for i in lista_precio:
        lista_precio_uf.append(i / uf_price)

    return lista_precio_uf

#Función que toma las listas de atributos, guarda estos en una estructura y las guarda en una lista.
def GetObjectList(lista_nombre, lista_info, lista_precio, uf_price):
    medicamentos = [] #Lista vacía que guardará los objetos.

    #Ciclo que recorres los atributos de las listas y los guarda en la nueva lista.
    for i in range(0, len(lista_nombre) - 1):
        med = M.Medicamento(lista_nombre[i], lista_info[i], lista_precio[i], uf_price) #Se crea el objeto medicamento.
        medicamentos.append(med)
    return medicamentos

