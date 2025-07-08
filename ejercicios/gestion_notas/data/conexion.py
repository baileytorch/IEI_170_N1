import mysql.connector
from mysql.connector import errorcode
from auxiliares.data_conexion import servidor,puerto,usuario,base_datos,contrasena

# Conectar con servidor
def generar_conexion(consulta):
    try:
        conexion = mysql.connector.connect(
            host = servidor,
            port = puerto,
            user = usuario,
            database = base_datos,
            password = contrasena)
        if conexion and conexion.is_connected():
            # return conexion
            cursor = conexion.cursor()
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
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

# # Crear un cursor
# def generar_cursor():
#     conexion = generar_conexion()
#     if conexion is not None:
#         cursor = conexion.cursor()
#         return cursor

# def manejo_data(consulta):
#     # Ejecutar comandos SQL
#     cursor = generar_cursor()
#     try:
#         if cursor is not None:
#             cursor.execute(consulta)
#             resultado = cursor.fetchall()
#             return resultado
#     except mysql.connector.Error as error:
#         print(error)