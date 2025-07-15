import mysql.connector
from mysql.connector import errorcode
from auxiliares.data_conexion import servidor, puerto, usuario, base_datos, contrasena

# Conectar con servidor


def generar_conexion():
    try:
        conexion = mysql.connector.connect(
            host=servidor,
            port=puerto,
            user=usuario,
            database=base_datos,
            password=contrasena)
        if conexion and conexion.is_connected():
            return conexion
        else:
            print('No ha sido posible conectarse con el servidor de base de datos')
    except mysql.connector.Error as error_conexion:
        if error_conexion.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Acceso denegado, usuario o contraseña incorrectos')
        elif error_conexion.errno == errorcode.ER_BAD_DB_ERROR:
            print('Su base de datos NO existe.')
        else:
            print(f'Ha ocurrido un error: {error_conexion}')
    else:
        conexion.close()


def leer_data(consulta):
    conexion = generar_conexion()
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            if cursor is not None:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                return resultado
        except mysql.connector.Error as error:
            print(error)
        conexion.close()


def insertar_data(consulta):
    conexion = generar_conexion()
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            if cursor != None:
                cursor.execute(consulta)
                conexion.commit()
                id = cursor.lastrowid
                cursor.close()
                return id
        except:
            print('No se ha podido guardar el dato en DB')
        conexion.close()
