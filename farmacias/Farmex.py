from bs4 import BeautifulSoup
import requests
from UF import UF
from farmacias import Farmacia as F

#Paquete de funciones para la farmacia Farmex.

class farmex(F.farmacia):

    #Función que retorna el número de páginas que se encontraron en la busqueda de cierto producto (query).
    def Get_LastPage(self, query):
        website = f'https://farmex.cl/search?page=1&q={query}+-tag%3Adelete&type=product' #Link de la página.
        response = requests.get(website) #Se obtienen los datos de la página
        soup = BeautifulSoup(response.content, 'html.parser') #Se convierte a texto.
        pags = soup.find('ul', {"class": 'pagination'}) #Se busca una parte en especifico del texto
        pags_li = pags.find_all('li')
        pages_num = int(pags_li[-2].text) #Número de páginas.
        return pages_num

    #Función que obtiene los datos de los productos de la página
    def getPage(self, i, query):
        website = f'https://farmex.cl/search?page={i}&q={query}+-tag%3Adelete&type=product' #Link de la página.
        response = requests.get(website) #Se obtienen los datos de la página.
        soup = BeautifulSoup(response.content, 'html.parser') #Se pasa a texto los datos de la página.
        meds = soup.find_all('div', {"class": 'product-grid-item'}) #Se busca donde están los productos.
        return meds

    #Procedimiento que va recorriendo las páginas de productos de la farmacia y los va almacenando en listas.
    def getData(self, num, query):
        banco = UF.BancoCentral("https://portalbiblioteca.bcentral.cl/web/banco-central/inicio") #Se crea la clase de banco
        price_uf = banco.find_Uf() #Se busca el valor de la UF.

        # Se instancian listas vacías que se irán llenando.
        meds_name = list()
        meds_info = list()
        meds_price = list()
        meds_farm = list()
        meds_price_uf = list()

        #Ciclo que va recorriendo las páginas de la farmacia.
        for i in range(num):
            i += 1

            meds = self.getPage(i, query) #Se obtiene el texto de los producto de cierta página.

            for med in meds: #Se recorren los productos y se van obtiendo sus atributos.

                info = med.find('h5', {"class": 'product-name'}).text.strip() #Descripción del producto.
                name = info[:info.index(" ")] #Nombre del producto.
                price = med.find('span', {"class": 'price'}) #Precio del producto.
                price_aux = med.find('span', {"class": 'price-compare'}) #Precio sin oferta si es que hay oferta.

                #Se van guardando las variables en lista dependiendo de las condiciones que se cumplan.
                if price is not None: #Si es que el precio está normal.
                    price = price.text.strip() #Extrae el texto de manera limpia.
                    price = int(price[1:].replace('.', ''))  # Precio se pasa de str a int.
                    meds_price.append(price) #Precio.
                    meds_info.append(info) #Descripción.
                    meds_name.append(name) #Nombre.
                    meds_farm.append("Farmex") #Farmacia.
                    meds_price_uf.append(price / price_uf)  #Precio en UF.

                elif price_aux is not None: #Si es que el precio está rebajado. (Se considera el precio sin oferta).
                    price = price_aux.text.strip() #Extrae el texto de manera limpia.
                    price = int(price[1:].replace('.', ''))  # Precio se pasa de str a int.
                    meds_price.append(price) #Precio
                    meds_info.append(info) #Descripción
                    meds_name.append(name) #Nombre
                    meds_farm.append("Farmex") #Farmacia
                    meds_price_uf.append(price / price_uf) #Precio en UF

        return meds_name, meds_info, meds_price, meds_farm, meds_price_uf

