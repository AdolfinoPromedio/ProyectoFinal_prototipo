import requests
from bs4 import BeautifulSoup

#Clase de Banco central, el cual tiene com oatributo el link de inicio de su página.
class BancoCentral:
    #Setter.
    def __init__(self, url):
        self.url = url

    #Función que encuentra y retorna el valor del UF en el url del banco central.
    def find_Uf(self):
        response = requests.get(self.url)
        if ((response.status_code==200)):
            soup = BeautifulSoup(response.content, 'html.parser')
            div1 = soup.find("p", {"class": "basic-text fs-2 f-opensans-bold text-center c-blue-nb-2"}).getText()
            UF = div1[1:].replace(".", "")
            UF = UF.replace(",", ".")
            return (float(UF))

        else :
            print("Falla en la conexión")
