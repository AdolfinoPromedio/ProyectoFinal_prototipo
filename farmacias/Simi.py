from bs4 import BeautifulSoup
import requests
from farmacias import Farmacia as F

#Paquete de funciones para la farmacia Dr. Simi.

class simi(F.farmacia):

    #Función que obtiene los datos de la página.
    def GetPage(self, i,query):
        website = f'https://www.drsimi.cl/catalogsearch/result/index/?p={str(i)}&q={query}' #Url de la página.
        response = requests.get(website) #Se extraen los datos.
        soup = BeautifulSoup(response.content, 'html.parser') #Se convierte a texto.
        return soup

    #Procedimiento que va recorriendo las páginas de productos de la farmacia y los va almacenando en listas los productos.
    def GetData(self, find):
        #Ciclo que va recorriendo las páginas.

        # Se instancian listas vacías que se irán llenando.
        lista_nombre = list()
        lista_info = list()
        lista_precio = list()
        lista_farmacia = list()

        for i in range(1, 10):
            soup = self.GetPage(i, find) #Se obtienen los datos de la página.

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
                lista_precio.append( int(precio[k].getText()[1:].replace('.', '')) ) #Precio.
                lista_farmacia.append('Dr. Simi') #Farmacia.

        return lista_nombre, lista_info, lista_precio, lista_farmacia  # Se retornan las listas.
