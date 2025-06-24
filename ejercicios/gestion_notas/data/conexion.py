import mysql.connector

# Conectar con servidor
conexion = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root")

# Crear un cursor
cursor_mysql = conexion.cursor()

# Ejecutar comandos SQL
# Execute a query
cursor_mysql.execute("SELECT CURDATE()")

# Fetch one result
row = cursor_mysql.fetchone()
print("Current date is: {0}".format(row))