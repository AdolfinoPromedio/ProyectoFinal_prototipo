from bs4 import BeautifulSoup
import requests
from farmacias import Farmacia as F

#Paquete de funciones para la farmacia Ahumada.

class ahumada(F.farmacia):

    #Función que va avanzando de página. Retorna el link de la página siguiente.
    def Get_NextPage(self, website):
        response = requests.get(website) #Obtiene los datos de la página.
        soup = BeautifulSoup(response.content, 'html.parser') #Los datos se pasan a texto.
        a_next_page = soup.find("a", {"class": "action next"}) #Se busca la parte donde está el link de la siguiente página.
        if (a_next_page is None):
            #Si se encuentra en la última página, retorna un 0.
            return 0
        else:
            return a_next_page.get('href') #Retorna el link.

    #Función que obtiene los datos del producto buscado (medicamento) y devuelve listas con todos los atributos encontrados.
    def GetData(self, medicamento):
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
                lista_precio.append( int(precio[k].getText()[1:].replace('.', '')) ) #Precio
                lista_farmacia.append('Ahumada') #Farmacia.

            #Se pasa a la siguiente página.
            website = self.Get_NextPage(website)

        lista_info = [" ".join(s.split()) for s in lista_info] #Se eliminan especios innecesarios.

        return lista_nombre, lista_info, lista_precio, lista_farmacia #Se retornan las listas.


