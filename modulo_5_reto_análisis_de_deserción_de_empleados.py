# Commented out IPython magic to ensure Python compatibility.
# %%writefile employees.py 
# #Importacion de liberias a utilizar
# import streamlit as st
# import pandas as pd
# import numpy as np
# import codecs 
# import matplotlib.pyplot as plt
# 
# st.title('Análisis de Deserción de Empleados') #Titulo principal
# st.header('Reto del Módulo 5') #Header de la pagina 
# st.write("""
# En esta página analizaremos el fenómeno de la
# deserción laboral y con ellos observaremos si provoca algun afectamiento a las empresas
# """) #Escribir una nota dentro de la pagina con una breve descripcion
# 
# DATE_COLUMN = 'released'
# DATA_URL = ('/content/drive/MyDrive/Data Science/Archivos Excel/Employees.csv') #Direccion del archivo
# 
# @st.cache #Funcion cache 
# def load_data(nrows): #Funcion a llamar con el numero de filas deseado 
#    #doc = codecs.open('/content/drive/MyDrive/Data Science/Archivos Excel/Employees.csv','rU','latin1') #Funcion codec para decodificar sin errores el archivo excel, en este excel no es necesaria 
#     data = pd.read_csv(DATA_URL, nrows=nrows) #Leer el archivo decodificado y con el numero de filas deseadas 
#     lowercase = lambda x: str(x).lower() #Pasar a minusculas 
#     return data #Regresar la informacion 
# 
# data_load_state = st.text('Loading employees data...') #Mensaje a mostrar cuando se esta cargando la informacion de nuestra pagina web 
# data = load_data(500) #Numero de filas seleccionadas a mostrar dentro de nuestra pagina web 
# data_load_state.text("Information displayed! (using st.cache)") #Mensaje a mostrar cuando la informacion se haya cargado por completo 
# #####################################################Filtros#############################################################################################################
# #Filtrado al dataframe original de acuerdo con la informacion proporcionada del usuario dentro de la columna Employee_ID
# def filter_data_by_employeeid(info): 
#     filtered_data_employeeid = data[data['Employee_ID'].str.upper().str.contains(info)] 
#     return filtered_data_employeeid
# 
# #Filtrado al dataframe original de acuerdo con la informacion proporcionada del usuario dentro de la columna Hometown
# def filter_data_by_hometown(info): 
#     filtered_data_hometown = data[data['Hometown'].str.capitalize().str.contains(info)]  
#     return filtered_data_hometown
#   
# #Filtrado al dataframe original de acuerdo con la informacion proporcionada del usuario dentro de la columna Unit
# def filter_data_by_unit(info): 
#     filtered_data_unit = data[data['Unit'].str.capitalize().str.contains(info)]  
#     return filtered_data_unit
# 
# #Filtrado al dataframe original de acuerdo con la informacion proporcionada del usuario dentro de la columna Education_level
# def filter_data_by_education(info): 
#     filtered_data_education = data[data['Education_Level'] == info] 
#     return filtered_data_education
# 
# #Filtrado al dataframe original de acuerdo con la informacion proporcionada del usuario dentro de la columna Hometown pero utilizando un selectbox
# def filter_data_by_home(info): 
#     filtered_data_home = data[data['Hometown'] == info] 
#     return filtered_data_home 
# 
# #Filtrado al dataframe original de acuerdo con la informacion proporcionada del usuario dentro de la columna Unit pero utilizando un selectbox
# def filter_data_by_un(info): 
#     filtered_data_un = data[data['Unit'] == info] 
#     return filtered_data_un 
# #####################################################Filtros#############################################################################################################
# 
# #####################################################-Sidebar-#############################################################################################################
# #Definicion de un sidebar
# sidebar = st.sidebar
# sidebar.title("Análisis Sidebar") #Titulo del sidebar
# sidebar.write("Opciones disponibles:") #Subtitulo del sidebar
# #####################################################-Checkbox-#############################################################################################################
# #Definicion del checkbox para mostrar u ocultar el dataframe original
# show_hide = sidebar.checkbox('Ocultar Tabla Original') #Checkbox a mostrar dentro del sidebar con su nombre 
# st.write("Ocultar tabla original:", show_hide)
# #st.markdown("___")
# 
# #Definicion del checkbox para el histograma 
# show_hide_hist = sidebar.checkbox('Mostrar el histograma por edad') #Checkbox a mostrar dentro del sidebar con su nombre 
# #st.markdown("___")
# 
# #Definicion del checkbox para la grafica de frecuencias
# show_hide_frec = sidebar.checkbox('Mostrar la grafica de frecuencias por unit') #Checkbox a mostrar dentro del sidebar con su nombre 
# #st.markdown("___")
# 
# #Definicion del checkbox para la grafica de hometown vs desercion
# show_hide_desercion = sidebar.checkbox('Mostrar la grafica de desercion por ciudad') #Checkbox a mostrar dentro del sidebar con su nombre 
# #st.markdown("___")
# 
# #Definicion del checkbox para la grafica de edad vs desercion
# show_hide_age = sidebar.checkbox('Mostrar la grafica de desercion por edad') #Checkbox a mostrar dentro del sidebar con su nombre 
# #st.markdown("___")
# 
# #Definicion del checkbox para la grafica de tiempo de servicio vs desercion
# show_hide_time = sidebar.checkbox('Mostrar la grafica de desercion por tiempo de servicio') #Checkbox a mostrar dentro del sidebar con su nombre 
# #st.markdown("___")
# #####################################################-Main Page-#############################################################################################################
# #####################################################-Main Code-#############################################################################################################
# ######Show-Hide Original Dataframe#################
# #Condicional para mostrar u ocultar el dataframe original haciendo uso del valor indicado por el usuario dentro del checkbox
# if show_hide:
#     #st.dataframe()
#     st.empty() 
#     st.header("") #Header de la pagina
# else: #Mostrar el dataframe original
#     st.header("Descripción de los datos (Tabla Original) ") #Header de la pagina
#     st.dataframe(data)
# ######TextBox and Command Botton#################
# #Creacion del text_input y boton para el apartado de busqueda por categoria: Employee_ID
# usuarioe = st.sidebar.text_input('Buscar por Employee_ID: ')
# btnBuscare = st.sidebar.button('Buscar por Employee_ID') #Poner un boton dentro del sidebar con el nombre de buscar 
# #st.markdown("___")
# 
# #Creacion del text_input y boton para el apartado de busqueda por categoria: Hometown
# usuarioh = st.sidebar.text_input('Buscar por Hometown: ')
# btnBuscarh = st.sidebar.button('Buscar por Hometown') #Poner un boton dentro del sidebar con el nombre de buscar 
# #st.markdown("___")
# 
# #Creacion del text_input y boton para el apartado de busqueda por categoria: Unit
# usuariou = st.sidebar.text_input('Buscar por Unit: ')
# btnBuscaru = st.sidebar.button('Buscar por Unit') #Poner un boton dentro del sidebar con el nombre de buscar 
# #st.markdown("___")
# 
# ######Main Code for TextBox and Command Botton#################
# #Condicional para llamar la funcion de filtrado y mostrar el dataframe con los valores deseados para Employee_ID
# if (btnBuscare):
#     st.header("Busqueda por Employee_ID ") #Header de la pagina
#     employeedata = filter_data_by_employeeid(usuarioe.upper()) 
#     count_row = employeedata.shape[0] # Gives number of rows
#     st.write(f'Total rows and employees: {count_row}')
#     data2=employeedata
#     st.dataframe(data2)
# else: 
#     st.empty()
# 
# #Condicional para llamar la funcion de filtrado y mostrar el dataframe con los valores deseados para Hometown
# if (btnBuscarh):
#     st.header("Busqueda por Hometown ") #Header de la pagina
#     hometowndata = filter_data_by_hometown(usuarioh.capitalize()) 
#     count_row = hometowndata.shape[0] # Gives number of rows
#     st.write(f'Total rows and employees: {count_row}')
#     data2=hometowndata
#     st.dataframe(data2)
# else: 
#     st.empty()
# 
# #Condicional para llamar la funcion de filtrado y mostrar el dataframe con los valores deseados para Unit    
# if (btnBuscaru):
#     st.header("Busqueda por Unit ") #Header de la pagina
#     unitdata = filter_data_by_unit(usuariou.capitalize()) 
#     count_row = unitdata.shape[0] # Gives number of rows
#     st.write(f'Total rows and employees: {count_row}')
#     data2=unitdata
#     st.dataframe(data2)
# else: 
#     st.empty()
# 
# ######SelectedBox#################
# ######Education_level#########
# #Creacion de un selectedbox para filtrar los empleados por su nivel educativo, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento
# selected_education = st.sidebar.selectbox("Selecciona el nivel educativo", data['Education_Level'].unique()) #Creacion del selectbox con las opciones de la columna de nivel educativo
# btnFilterbyEducation = st.sidebar.button('Filtrar educacion ') #Crear un button con el nombre de filtrar educacion 
# 
# if (btnFilterbyEducation): #Condicional del boton de filtrado por nivel educativo
#     st.header("Busqueda por nivel educativo ") #Header de la pagina
#     filterbyedu = filter_data_by_education(selected_education) #llamado a la funcion de filtrar por nivel de educacion mandando la seleccion propuesta por el usuario dentro del selectbox
#     count_row = filterbyedu.shape[0]  # Gives number of rows
#     st.write(f"Total rows and employees : {count_row}")
#     st.dataframe(filterbyedu)
# else: 
#     st.empty()
# 
# ######Hometown#########
# #Creacion de un selectedbox para filtrar los empleados por su ciudad, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento
# selected_hometown = st.sidebar.selectbox("Selecciona una ciudad participante", data['Hometown'].unique()) #Creacion del selectbox con las opciones de la columna de Hometown
# btnFilterbyHometown = st.sidebar.button('Filtrar por ciudad ') #Crear un button con el nombre de filtrar por ciudad 
# 
# if (btnFilterbyHometown): #Condicional del boton de filtrado por nivel educativo
#     st.header("Busqueda por ciudad participante ") #Header de la pagina
#     filterbyhome = filter_data_by_home(selected_hometown) #llamado a la funcion de filtrar por ciudad participante mandando la seleccion propuesta por el usuario dentro del selectbox
#     count_row = filterbyhome.shape[0]  # Gives number of rows
#     st.write(f"Total rows and employees : {count_row}")
#     st.dataframe(filterbyhome)
# else: 
#     st.empty()
# 
# ######Unit#########
# #Creacion de un selectedbox para filtrar los empleados por su unit, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento
# selected_un = st.sidebar.selectbox("Selecciona una unit de los empleados", data['Unit'].unique()) #Creacion del selectbox con las opciones de la columna de Unit
# btnFilterbyunit = st.sidebar.button('Filtrar por unit ') #Crear un button con el nombre de filtrar por unit 
# 
# if (btnFilterbyunit): #Condicional del boton de filtrado por unit
#     st.header("Busqueda por unit ") #Header de la pagina
#     filterbyun = filter_data_by_un(selected_un) #llamado a la funcion de filtrar por ciudad participante mandando la seleccion propuesta por el usuario dentro del selectbox
#     count_row = filterbyun.shape[0]  # Gives number of rows
#     st.write(f"Total rows and employees : {count_row}")
#     st.dataframe(filterbyun)
# else: 
#     st.empty()
# 
# ######Histograma#################
# if show_hide_hist:
# #El rango mas comun de edades de acuerdo al histograma mostrado seria entre los 20 y 30 años, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento
#     st.subheader('Agrupacion de empleados por edad') #Titulo de cuando se despliegue 
#     fig, ax = plt.subplots() 
#     ax.hist(data['Age'], bins=[10,20,30,40,50,60,70], color="blue") #Realizacion de histograma de acuerdo a la columna de edades 
#     st.header("Histograma de edades") #Header del histograma 
#     plt.ylabel('Edades', fontsize=15, color='red') #Ylabels edicion 
#     plt.xlabel('Catidad de Empleados', fontsize=15, color='red') #Xlabels edicion 
#     plt.grid(True) #Poner grid en la grafica 
#     st.pyplot(fig)
#     st.text("El rango mas comun de edades de acuerdo al histograma mostrado seria entre los 20 y 30 años, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento")
# else: 
#     st.empty()
# 
# ######Grafica de frecuencias#################
# #Crear una gráfica de frecuencias para las unidades funcionales (Unit) para conocer cuántos empleados hay en cada Unidad, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento
# if show_hide_frec:
# #De acuerdo al histograma en la unidad de IT se encuentra el mayor numero de empleados
#     st.subheader('Agrupacion de empleados por unit') #Titulo de cuando se despliegue 
#     fig, ax = plt.subplots() 
#     ax.hist(data['Unit'], bins=range(0,12+2), color="black") #Realizacion de histograma de acuerdo a la columna de unit 
#     st.header("Grafico de frecuencias por unit") #Header del histograma 
#     plt.ylabel('Unit', fontsize=15, color='red') #Ylabels edicion 
#     plt.xlabel('Catidad de Empleados', fontsize=15, color='red') #Xlabels edicion 
#     plt.xticks(rotation = 90, color="blue") #Xlabels edicion 
#     plt.grid(True) #Poner grid en la grafica 
#     st.pyplot(fig)
#     st.text("De acuerdo al histograma en la unidad de IT se encuentra el mayor numero de empleados")
# else: 
#     st.empty()
# 
# ######Grafica para visualizar las ciudades que tienen el mayor indice de desercion#################
# #Analizar los datos con una gráfica que nos permita visualizar las ciudades (Hometown) que tienen el mayor índice de deserción 
# #La ciudad con mayor indice de desercion es Clinton con 0.2033%, lo podemos encontrar en la grafica, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento
# if show_hide_desercion:
#     employees_by_hometown = data.groupby('Hometown').mean() #Crear un nuevo dataframe que contenga el promedio de los valores de cada columna agrupado por la columna Hometown
#     indice_desercion = employees_by_hometown[['Attrition_rate']]
#     indice_desercion = indice_desercion.rename_axis('Hometown').reset_index()
#     st.subheader('Agrupacion de desercion por ciudad') #Titulo de cuando se despliegue 
#     fig2, ax2 = plt.subplots()
#     y_pos = indice_desercion['Attrition_rate']
#     x_pos = indice_desercion['Hometown']
#     ax2.barh(x_pos, y_pos, color="orange")
#     ax2.set_xlabel('Desercion', fontsize=15, color='red')
#     ax2.set_ylabel('Ciudades', fontsize=15, color='red')
#     st.header("Grafico de desercion por ciudad")
#     plt.xticks(rotation = 90, color="blue")
#     plt.grid(True)
#     st.pyplot(fig2)
#     st.text("La ciudad con mayor indice de desercion es Clinton con 0.2033%, lo podemos encontrar en la grafica, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento")
# else: 
#     st.empty()
# 
# ######Grafica para visualizar la tasa de desercion de acuerdo a la edad#################
# #Analizar la información con una gráfica que permita visualizar la edad y la tasa de deserción
# ##La edad con mayor indice de desercion es 23 años con 0.364975%, lo podemos encontrar en la grafica, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento
# if show_hide_age:
#     employees_by_age = data.groupby('Age').mean() #Crear un nuevo dataframe que contenga el promedio de los valores de cada columna agrupado por la columna Hometown
#     indice_deserciona = employees_by_age[['Attrition_rate']]
#     indice_deserciona = indice_deserciona.rename_axis('Age').reset_index()
#     st.subheader('Agrupacion de desercion por edad') #Titulo de cuando se despliegue 
#     fig2, ax2 = plt.subplots()
#     y_pos = indice_deserciona['Attrition_rate']
#     x_pos = indice_deserciona['Age']
#     ax2.barh(x_pos, y_pos, color="purple")
#     ax2.set_xlabel('Desercion', fontsize=15, color='red')
#     ax2.set_ylabel('Edades', fontsize=15, color='red')
#     st.header("Grafico de desercion por edad")
#     #plt.xticks(indice_deserciona['Attrition_rate'])
#     plt.xticks(rotation = 90, color="red")
#     #plt.xscale("log")
#     st.pyplot(fig2)
#     st.text("La edad con mayor indice de desercion es 23 años con 0.364975%, lo podemos encontrar en la grafica, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento")
# else: 
#     st.empty()
# 
# #Analizar con una gráfica que determine la relación entre el tiempo de servicio y la tasa de deserción 
# ##La edad con mayor indice de desercion es 26 años de tiempo de servicio con 0.2676%, lo podemos encontrar en la grafica, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento
# if show_hide_time:
#     employees_by_time = data.groupby('Time_of_service').mean() #Crear un nuevo dataframe que contenga el promedio de los valores de cada columna agrupado por la columna Hometown
#     indice_deserciont = employees_by_time[['Attrition_rate']]
#     indice_deserciont = indice_deserciont.rename_axis('Time_of_service').reset_index()
#     st.subheader('Agrupacion de desercion por tiempo de servicio') #Titulo de cuando se despliegue 
#     fig2, ax2 = plt.subplots()
#     y_pos = indice_deserciont['Attrition_rate']
#     x_pos = indice_deserciont['Time_of_service']
#     ax2.barh(x_pos, y_pos, color="skyblue")
#     ax2.set_xlabel('Desercion', fontsize=15, color='red')
#     ax2.set_ylabel('Tiempo de servicio', fontsize=15, color='red')
#     st.header("Grafico de desercion por tiempo de servicio")
#     plt.xticks(rotation = 90, color="red")
#     st.pyplot(fig2)
#     st.text("La edad con mayor indice de desercion es 26 años de tiempo de servicio con 0.2676%, lo podemos encontrar en la grafica, es importante mencionar que este resultado obtenido es de acuerdo al dataframe original con las unicas 500 primeras filas del documento")
# else: 
#     st.empty()

"""Una vez cargado y ejecutado el archivo ahora vamos a proceder a ejecutarlo con el comando streamlit para que se visualice el contenido del mismo."""

