import sqlite3

# Paso 1, conectar con DB SQLite, si no existe, se creará
conexion = sqlite3.connect('gestion_notas.db')

# Paso 2, creamos un cursor para interactuar con la DB
cursor = conexion.cursor()

# Cerrar la conexión a la DB
conexion.close()