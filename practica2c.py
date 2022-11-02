# Reemplazar ... por el código correspondiente

import psycopg2

import pandas as pd


def dbConectar():
    ip = "localhost"
    puerto = 5432
    basedatos = "Habitantes"

    usuario = "postgres"
    contrasena = "12345"

    print("---dbConectar---")
    print("---Conectando a Oracle---")

    try:
        conexion = psycopg2.connect(user=usuario, password=contrasena, host=ip, port=puerto, database=basedatos)
        print("Conexión realizada a la base de datos", conexion)
        return conexion
    except psycopg2.DatabaseError as error:
        print("Error en la conexión")
        print(error)
        return None


# ------------------------------------------------------------------

def dbDesconectar():
    print("---dbDesconectar---")
    try:
        conexion.commit()
        conexion.close()
        print("Desconexión realizada correctamente")
        return True
    except psycopg2.DatabaseError as error:
        print("Error en la desconexión")
        print(error)
        return False


# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

def ImportarSQL(consulta, conex):
    print('---ImportarSQL---')
    try:
        df = pd.read_sql(consulta, conex)
        print(df)
        return (df)
    except psycopg2.DatabaseError as error:
        print("Error. No se ha podido importar de SQL")
        print(error)


# ------------------------------------------------------------------

def ExportarExcel(ruta, df):
    print('---ExportarExcel---')
    try:
        # index a False para no escribir la columna índice
        df.to_excel(ruta, index=False)
    except psycopg2.DatabaseError as error:
        print("Error. No se ha podido exportar a Excel")
        print(error)


# ------------------------------------------------------------------

def ImportarExcel(ruta):
    print('---ImportarExcel---')
    try:
        df = pd.read_excel(ruta)
        print(df)
        return (df)
    except ... as error:
        print("Error. No se ha podido importar de Excel")
        print(error)


# ------------------------------------------------------------------

def ExportarCSV(ruta, df):
    print('---ExportarCSV---')
    try:
        # index a False para no escribir la columna índice
        df.to_csv(ruta, index=False)
    except ... as error:
        print("Error. No se ha podido exportar a CSV")
        print(error)


# ------------------------------------------------------------------

def ImportarCSV(ruta):
    print('---ImportarCSV---')
    try:
        df = pd.read_csv(ruta)
        print(df)
        return (df)
    except ... as error:
        print("Error. No se ha podido importar de CSV")
        print(error)


# ------------------------------------------------------------------

def ExportarJson(ruta, df):
    print('---ExportarJson---')
    try:
        df.to_json(ruta)
    except ... as error:
        print("Error. No se ha podido exportar a Json")
        print(error)


# ------------------------------------------------------------------

def ImportarJson(ruta):
    print('---ImportarJson---')
    try:
        df = pd.read_json(ruta)
        print(df)
        return (df)
    except ... as error:
        print("Error. No se ha podido importar de Json")
        print(error)


# ------------------------------------------------------------------

def dfConsultarAtributos(df):
    print("---dfConsultarAtributos---")
    try:
        print('head')
        # Por defecto muestra 5 elementos
        print(df.head(3))  # Mostrar los 3 primeros elementos

        print('tail')
        # Por defecto muestra 5 elementos
        print(df.tail())

        print('info')
        print(df.info())

        print('shape')
        print(df.shape)

        print('size')
        print(df.size)

        print('columns')
        print(df.columns)

        print('index')
        print(df.index)

        print('dtypes')
        print(df.dtypes)

    except ... as error:
        print("Error. Problema en atributos de dataFrame")
        print(error)


# ------------------------------------------------------------------

def dfDiccionarioDeListas():
    print("---dfDiccionarioDeListas---")
    try:
        datos = {'CODS': [5, 6, 7], \
                 'NOMBRES': ['Deportes', 'Autónomo', 'Tecnológicas'], \
                 'PORCENTS': [0.0, 0.0, 0.0], \
                 'INGRESOSS': [110.2, 111.1, 112.2]}
        df = pd.DataFrame(datos)
        print(df)
        return (df)

    except ... as error:
        print("Error. Problema en DataFrame a partir de Diccionario de Listas")
        print(error)


# ------------------------------------------------------------------

def dfListaDeListas():
    print("---dfListaDeListas---")

    try:
        df = pd.DataFrame([[8, 'Finanzas', 0.0, 120.1], \
                           [9, 'Banca', 0.0, 121.2], \
                           [10, 'Energía', 0.0, 122.3]], \
                          columns=['CODS', 'NOMBRES', 'PORCENTS', 'INGRESOSS'])
        print(df)
        return (df)

    except ... as error:
        print("Error. Problema en DataFrame a partir de Lista de Listas")
        print(error)


# ------------------------------------------------------------------

def dfListaDeDiccionarios():
    print("---dfListaDeDiccionarios---")

    try:
        df = pd.DataFrame([{'CODS': 11, \
                            'NOMBRES': 'Educación', \
                            'PORCENTS': 0.0, \
                            'INGRESOSS': 130.1}, \
                           {'CODS': 12, \
                            'NOMBRES': 'Sanidad', \
                            'PORCENTS': 0.0, \
                            'INGRESOSS': 131.2}, \
                           {'CODS': 13, \
                            'NOMBRES': 'Seguridad', \
                            'PORCENTS': 0.0, \
                            'INGRESOSS': 132.3}])
        print(df)
        return (df)

    except ... as error:
        print("Error. Problema en DataFrame a partir de Lista de Diccionarios")
        print(error)


# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

print("---Programa principal---")

conexion = dbConectar()

if (conexion is None):
    print("ERROR DE CONEXIÓN")
else:
    print("CONEXIÓN REALIZADA")

    # Crear DataFrame a partir de una consulta
    consulta = pd.read_sql('select dni,nombre,sector from Poblacion', conexion)
    print(consulta)

    # Crear DataFrame desde una consulta a base de datos
    consulta = 'select * from Poblacion'
    pob = ImportarSQL(consulta, conexion)
    consulta = 'select * from Sectores'
    sec = ImportarSQL(consulta, conexion)

    # Consultar atributos de DataFrame
    dfConsultarAtributos(pob)
    dfConsultarAtributos(sec)

    # Exportar e importar DataFrame a/desde formatos útiles
    rutapob = 'c:\\trabajo\\Poblacion.'
    rutasec = 'c:\\trabajo\\Sectores.'

    ExportarExcel(rutapob + 'xlsx', pob)
    ExportarExcel(rutasec + 'xlsx', sec)

    pob = ImportarExcel(rutapob + 'xlsx')
    sec = ImportarExcel(rutasec + 'xlsx')

    ExportarCSV(rutapob + 'csv', pob)
    ExportarCSV(rutasec + 'csv', sec)

    pob = ImportarCSV(rutapob + 'csv')
    sec = ImportarCSV(rutasec + 'csv')

    ExportarJson(rutapob + 'json', pob)
    ExportarJson(rutasec + 'json', sec)

    pob = ImportarJson(rutapob + 'json')
    sec = ImportarJson(rutasec + 'json')

    # Añadir filas
    sec2 = dfDiccionarioDeListas()
    dfConsultarAtributos(sec2)

    sec3 = dfListaDeListas()
    dfConsultarAtributos(sec3)

    sec4 = dfListaDeDiccionarios()
    dfConsultarAtributos(sec4)

    sec5 = pd.concat([sec, sec2, sec3, sec4])
    print('---Después de concat---')
    print(sec5)  # Observar índices de DataFrame repetidos

    # Añadir filas
    # Añadiendo un diccionario
    datos = {'CODS': 14, \
             'NOMBRES': 'Aeronáutica', \
             'PORCENTS': 0.0, \
             'INGRESOSS': 1010}
    sec5 = sec5.append(datos, ignore_index=True)  # Inserción
    print('---Después de append---')
    print(sec5)  # Observar índices de DataFrame NO repetidos
    # Añadiendo una lista
    datos = [15, 'Náutico', 0.0, 1200.0]
    print(datos)
    indice = len(sec5)
    print("Índice:", indice)
    sec5.loc[indice] = datos  # Inserción
    print(sec5)  # Observar índices de DataFrame NO repetidos

    # Accesos
    print('---Accessos---')
    print('Mostrar columna:')
    print(sec5['NOMBRES'])
    print(sec5[['NOMBRES', 'INGRESOSS']])  # Ojo con el doble [] cuando hay más de una columna!!!
    print('Mostrar fila (accediendo por índice):')
    print(sec5.loc[4])
    print('Mostrar fila (accediendo por valor):')
    print(sec5.loc[sec5['CODS'] == 14])
    print(sec5.loc[sec5['NOMBRES'] == 'Náutico'])

    # Ordenar
    print('---Ordenar---')
    sec5 = sec5.sort_values(by=['INGRESOSS'], ascending=False)
    print(sec5)

    # Duplicados
    print('---Duplicados---')
    print('Mostrar duplicados en columna INGRESOSS:')
    print(sec5.duplicated('INGRESOSS'))
    print('Eliminar duplicados:')
    sec6 = sec5.drop_duplicates(subset=['INGRESOSS'])
    print(sec5)
    print(sec6)

    # Borrar filas
    print('---Borrar filas---')
    print('Eliminar filas por índice')
    print(sec6.loc[14])
    sec6 = sec6.drop([14])  # Eliminar 'Náutico'
    print('Eliminar filas por valor')
    indice = sec5.loc[sec5['NOMBRES'] == 'Banca']
    print(indice)
    print(indice.NOMBRES)
    sec6 = sec6.drop(indice.index)  # Eliminar 'Banca'
    print(sec6)

    # Funciones
    print('---Funciones---')
    print('Suma', sec6['INGRESOSS'].sum())
    print('Valores únicos', sec6['INGRESOSS'].nunique())
    print('Contar valores', sec6['INGRESOSS'].count())
    print('Valor máximo', sec6['INGRESOSS'].max())
    print('Valor mínimo', sec6['INGRESOSS'].min())
    print('Media', sec6['INGRESOSS'].mean())
    print('Mediana', sec6['INGRESOSS'].median())
    print('Moda', sec6['INGRESOSS'].mode())
    print('Cuartiles', sec6['INGRESOSS'].quantile())
    print('Varianza', sec6['INGRESOSS'].var())
    print('Asimetría de Fisher', sec6['INGRESOSS'].skew())
    print('Curtosis', sec6['INGRESOSS'].kurtosis())
    print('Desviación estándar', sec6['INGRESOSS'].std())
    print('Correlación de Pearson', sec6['INGRESOSS'].corr(sec6['INGRESOSS']))
    print('Estadística descriptiva')
    print(sec6['INGRESOSS'].describe())
    print('Funciones de agregación personalizadas')
    print(sec6['INGRESOSS'].agg(['sum', 'max', 'min', 'mean', 'var']))
    print('Funciones de cadenas')
    print(sec6['NOMBRES'].str.lower())
    print(sec6['NOMBRES'].str.upper())

    dbDesconectar()

print("---Fin de programa---")