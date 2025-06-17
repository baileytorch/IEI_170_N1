import sqlite3

with sqlite3.connect('gestion_notas.db') as conexion:

    cursor = conexion.cursor()

    crear_tabla_docentes = '''
    CREATE TABLE IF NOT EXISTS docentes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rut TEXT NOT NULL,
        nombre TEXT NOT NULL
    );
    '''

    crear_tabla_asignaturas = '''
    CREATE TABLE IF NOT EXISTS asignaturas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL,
        nombre TEXT NOT NULL,
        id_docente INTEGER,
        FOREIGN KEY (id_docente) references docentes(id)
    );
    '''

    insertar_datos_docentes = '''
    INSERT INTO docentes (rut,nombre) VALUES ('12345678-5','Aquiles Baeza');
    '''
    insertar_datos_asignaturas = '''
    INSERT INTO asignaturas (codigo,nombre,id_docente) VALUES ('BIO','Biología',1);
    '''

    comandos = [crear_tabla_docentes,crear_tabla_asignaturas,insertar_datos_docentes,insertar_datos_asignaturas]
    for comando in comandos:
        cursor.execute(comando)
        conexion.commit()
        print("Tabla creada exitosamente!")