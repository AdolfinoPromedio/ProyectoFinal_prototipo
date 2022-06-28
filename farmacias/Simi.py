from bs4 import BeautifulSoup
import requests
from medicamentos import medicamento as M

#Paquete de funciones para la farmacia Dr. Simi.

#Función que obtiene los datos de la página.
def GetPage(i,query):
    website = f'https://www.drsimi.cl/catalogsearch/result/index/?p={str(i)}&q={query}' #Url de la página.
    response = requests.get(website) #Se extraen los datos.
    soup = BeautifulSoup(response.content, 'html.parser') #Se convierte a texto.
    return soup

#Procedimiento que va recorriendo las páginas de productos de la farmacia y los va almacenando en listas los productos.
def GetData(lista_nombre, lista_info, lista_precio, farmacia, find):
    #Ciclo que va recorriendo las páginas.
    for i in range(1, 10):
        soup = GetPage(i, find) #Se obtienen los datos de la página.

        #Se buscan los atributos.
        nombre = soup.find_all('a', {"class": 'product-item-link'}) #Nombre
        info = soup.find_all('a', {"class": 'product-item-link'}) #Descripción
        precio = soup.find_all('span', {"class": 'price'}) #Precio

        #Si el largo los nombres encontrados es 0, significa que no hay más productos a encontrar, por lo cual se termina el ciclo.
        if len(nombre) == 0:
            break
        #En caso contrario, se guardan los atributos en las listas.
        for k in range(len(nombre)):
            lista_nombre.append(find) #Nombre.
            lista_info.append(info[k].getText()) #Descrición.
            lista_precio.append(precio[k].getText()) #Precio.
            farmacia.append('Dr. Simi') #Farmacia.

#Función que recorre las listas de precios, los transforma a UF y luego los almacena en otra lista. Retorna esta lista.
def precio_to_UF(lista_precio, uf_price):
    lista_precio_uf = [] #Lista vacía.
     #Ciclo que recorrerá la lista de precio, lo convierte a números y calcula el precio en UF, guardandolo en la lista.
    for i in lista_precio:
        precio = int(i[1:].replace('.', '')) #Se convierte de str a int.
        lista_precio_uf.append(precio / uf_price) #Se guarda.
    return lista_precio_uf

#Función que toma las listas de atributos, guarda estos en una estructura y las guarda en una lista.
def GetObjectList(lista_nombre, lista_info, lista_precio, uf_price):
    medicamentos = []#Lista vacía que guardará los objetos.

    #Ciclo que recorres los atributos de las listas y los guarda en la nueva lista.
    for i in range(0, len(lista_nombre)-1):
        med = M.Medicamento(lista_nombre[i], lista_info[i], lista_precio[i], uf_price) #Se crea el objeto medicamento.
        medicamentos.append(med)
    return medicamentos
