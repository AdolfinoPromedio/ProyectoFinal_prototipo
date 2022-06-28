from UF import UF
from data_manager import Archivo as A
from farmacias import Simi
from farmacias import Ahumada
from farmacias import Farmex

#Variables:

path = r'C:\Users\drago\PycharmProjects\Scrapping' #Ruta donde se irán guardando los csv.
banco = UF.BancoCentral("https://portalbiblioteca.bcentral.cl/web/banco-central/inicio") #Se crea el objeto de banco.
uf_price = banco.find_Uf() #Se obtiene el valor de la UF.
find = 'Paracetamol' #Lo que se quiere buscar.
manager = A.Archivo() #Se crea el manager de archivos.

#Se crean listas vacías que se irán llenando con los atributos de los productos.
lista_nombre = list()
lista_info = list()
lista_precio = list()
lista_farmacia = list()

#Farmacia Dr. Simi.

Simi.GetData(lista_nombre, lista_info, lista_precio, lista_farmacia, find) #Se obtienen los datos del producto buscado de la farmacia y se guardan en las listas antes creadas.
lista_precio_uf = Simi.precio_to_UF(lista_precio, uf_price) #Se crea la lista de precios UF de cada producto.
df_simi = manager.toDF(lista_nombre, lista_info, lista_precio, lista_precio_uf, lista_farmacia) #Se crea el data frame con los datos.
manager.toCSV(df_simi, 'Dr. Simi', path) #Se crea un archivo csv con los datos extraidos.
medicamentos_simi =  Simi.GetObjectList(lista_nombre, lista_info, lista_precio, uf_price) #Se crea una lista de objetos 'medicamento' con los datos de los productos.

####################

#Farmacia Ahumada

lista_nombre, lista_info, lista_precio, lista_farmacia = Ahumada.GetData(find) #Se obtienen los datos del producto buscado de la farmacia y se guardan en las listas antes creadas.
lista_precio_uf = Ahumada.precio_to_UF(lista_precio, uf_price) #Se crea la lista de precios UF de cada producto.
df_ahumada = manager.toDF(lista_nombre, lista_info, lista_precio, lista_precio_uf, lista_farmacia) #Se crea el data frame con los datos.
manager.toCSV(df_ahumada, 'Ahumada', path) #Se crea un archivo csv con los datos extraidos.
medicamentos_ahumada = Ahumada.GetObjectList(lista_nombre, lista_info, lista_precio, uf_price) #Se crea una lista de objetos 'medicamento' con los datos de los productos.

###################

#Farmacia Farmex

#Se vacían las listas
lista_nombre = list()
lista_info = list()
lista_precio = list()
lista_farmacia = list()
lista_precio_uf = list()

Farmex.getData(Farmex.Get_LastPage(find), find, lista_nombre, lista_info, lista_precio, lista_farmacia,lista_precio_uf) #Se obtienen los datos del producto buscado de la farmacia y se guardan en las listas antes creadas.
df_farmex = manager.toDF(lista_nombre, lista_info, lista_precio, lista_precio_uf, lista_farmacia) #Se crea el data frame con los datos.
manager.toCSV(df_farmex, 'Farmex', path) #Se crea un archivo csv con los datos extraidos.
medicamentos_farmex = Farmex.GetObjectList(lista_nombre, lista_info, lista_precio, uf_price) #Se crea una lista de objetos 'medicamento' con los datos de los productos.

###################

#csv final.
df_final = manager.joinDF(df_simi, df_farmex, df_ahumada) #Se juntan los dataframes de las farmacias en uno solo.
manager.toCSV(df_final, 'Final', path) #Se crea un archivo csv con los datos finales.