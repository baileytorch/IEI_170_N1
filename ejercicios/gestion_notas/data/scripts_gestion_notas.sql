CREATE TABLE IF NOT EXISTS docentes(
    id_docente INT AUTO_INCREMENT,
    nombre_docente VARCHAR(255) NOT NULL,
    rut_docente INTEGER NOT NULL UNIQUE,
    digito_verificador VARCHAR(1) NOT NULL,
    email_docente VARCHAR(255) NULL,

    CONSTRAINT PK_docentes PRIMARY KEY (id_docente)
);

CREATE TABLE IF NOT EXISTS asignaturas(
    id_asignatura INT AUTO_INCREMENT,
    codigo_asignatura VARCHAR(3) NOT NULL UNIQUE,
    nombre_asignatura VARCHAR(255) NOT NULL,
    id_docente INTEGER NULL,

    CONSTRAINT PK_asignaturas PRIMARY KEY (id_asignatura),
    CONSTRAINT FK_docentes FOREIGN KEY (id_docente) REFERENCES docentes(id_docente)
);

INSERT INTO docentes (nombre_docente,rut_docente,digito_verificador) VALUES 
('Aquiles Baeza',12345678,'5'),
('Wendy Sulca',13630677,'4'),
('Erick Bailey',12824290,'2');

SELECT * FROM DOCENTES;

INSERT INTO ASIGNATURAS (codigo_asignatura,nombre_asignatura) VALUES 
('BIO','Biología Celular'),
('QUI','Química Orgánica'),
('FIS','Cinemática');

SELECT * FROM ASIGNATURAS;
