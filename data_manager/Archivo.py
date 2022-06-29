import pandas as pd

#Clase que hace el manejo de archivos. Principalmente crea dataframes. Además crea y lee archivos csv.
class Archivo:

    #Función que crea un data frame en base a listas.
    def toDF(self, lista_nombre, lista_info, lista_precio, lista_precio_uf, lista_farmacia):

        #Dependiendo de la farmacia que sea, el dataframe será creado de cierta manera.
        if lista_farmacia[0] =='Dr. Simi': #Farmacia Dr Simi.
            df = pd.DataFrame({'Nombre': lista_nombre, 'Info':lista_info,"Precio":lista_precio, "Precio UF": lista_precio_uf, 'Farmacia':lista_farmacia})
            df["Info"] = df["Info"].apply(lambda x: x.strip("\n").strip(" ")) #Esto es para quitar espacios en blancos innecesarios.
            df["Nombre"] = df["Nombre"].apply(lambda x: x.strip("\n").strip(" "))
            return df

        elif lista_farmacia[0] == 'Ahumada': #Farmacia Ahumada.
            df = pd.DataFrame({'Nombre': lista_nombre, 'Info': lista_info, "Precio": lista_precio, "Precio UF": lista_precio_uf, 'Farmacia': lista_farmacia})
            return df

        elif lista_farmacia[0] == 'Farmex': #Farmacia Farmex
            df = pd.DataFrame({'Nombre': lista_nombre, 'Info': lista_info, "Precio": lista_precio, "Precio UF": lista_precio_uf, 'Farmacia': lista_farmacia})
            return df

    #Función que junta dataframes y los junta en uno.
    def joinDF(self, df1, df2, df3):
        frames = [df1, df2, df3]
        dataframe = pd.concat(frames)
        return dataframe

    #Función que lee un archivo CVS.
    def ReadCVS(self, path,file):
        my_file = open(path + '\\' +file, "r", encoding='utf-8')
        content_list = my_file.readlines()
        for i in range(0,(len(content_list)-1)):
            content_list[i] = content_list[i][:-1]
        return content_list

    #Función que convierte un dataframe en un archivo .csv
    def toCSV(self, df, farmacia, path, i):

        #Dependiendo de la farmacia, se creará un archivo con un nombre distinto.
        if farmacia == 'Dr. Simi':
            df.to_csv(path + '\data_DrSimi.csv', index=False)

        elif farmacia == 'Farmex':
            df.to_csv(path + '\data_Farmex.csv', index=False)

        elif farmacia == 'Ahumada':
            df.to_csv(path + '\data_Ahumada.csv', index=False)

        elif farmacia == 'Final':
            df.to_csv(path + '\medicamentos' + str(i) + '.csv', index=False)

        elif farmacia == 'no farmacia':
            df.to_csv(path + '\parámetros.csv' , index=False)
