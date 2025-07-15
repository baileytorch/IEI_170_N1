CREATE TABLE IF NOT EXISTS docentes(
    id_docente INT AUTO_INCREMENT,
    nombre_docente VARCHAR(255) NOT NULL,
    rut_docente INTEGER NOT NULL UNIQUE,
    digito_verificador VARCHAR(1) NOT NULL,
    email_docente VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT PK_docentes PRIMARY KEY (id_docente)
);

CREATE TABLE IF NOT EXISTS asignaturas(
    id_asignatura INT AUTO_INCREMENT,
    codigo_asignatura VARCHAR(3) NOT NULL UNIQUE,
    nombre_asignatura VARCHAR(255) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,

    CONSTRAINT PK_asignaturas PRIMARY KEY (id_asignatura)
);

CREATE TABLE IF NOT EXISTS docentes_asignaturas(
    id_docente_asignatura INT AUTO_INCREMENT,
    id_docente INT NOT NULL,
    id_asignatura INT NOT NULL,

    CONSTRAINT pk_docentes_asignaturas PRIMARY KEY (id_docente_asignatura),
    CONSTRAINT fk_tabla_docentes FOREIGN KEY (id_docente) REFERENCES docentes (id_docente),
    CONSTRAINT fk_tabla_asignaturas FOREIGN KEY (id_asignatura) REFERENCES asignaturas (id_asignatura)
)

CREATE TABLE IF NOT EXISTS opciones_menu(
    id_opcion_menu INT AUTO_INCREMENT,
    opcion_menu VARCHAR(250) NOT NULL,
    numero_opcion INT NOT NULL,
    tipo_menu INT NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    
    CONSTRAINT pk_opciones_menu PRIMARY KEY (id_opcion_menu)
);