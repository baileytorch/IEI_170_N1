CREATE TABLE IF NOT EXISTS docentes(
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    rut INTEGER NOT NULL UNIQUE,
    digito_verificador VARCHAR(1) NOT NULL,
    email VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS asignaturas(
    id INTEGER PRIMARY KEY,
    codigo_asignatura VARCHAR(3) NOT NULL UNIQUE,
    nombre_asignatura VARCHAR(255) NOT NULL,
    id_docente INTEGER NULL,
    FOREIGN KEY (id_docente) REFERENCES docentes(id)
);

ALTER TABLE docentes ADD COLUMN email_docente;

ALTER TABLE docentes RENAME COLUMN nombre TO nombre_docente;

ALTER TABLE docentes RENAME COLUMN rut TO rut_docente;

ALTER TABLE docentes RENAME COLUMN email TO email_docente;

INSERT INTO docentes (ID,NOMBRE_DOCENTE,RUT_DOCENTE,DIGITO_VERIFICADOR) VALUES 
(1,'Aquiles Baeza',12345678,'5'),
(2,'Wendy Sulca',13630677,'4'),
(3,'Erick Bailey',12824290,'2');

SELECT * FROM DOCENTES;

INSERT INTO ASIGNATURAS (ID,CODIGO_ASIGNATURA,NOMBRE_ASIGNATURA,ID_DOCENTE) VALUES 
(1,'BIO','Biología Celular',1),
(2,'QUI','Química Orgánica',2),
(3,'FIS','Cinemática',3);

SELECT * FROM ASIGNATURAS;

SELECT 
    ASIG.CODIGO_ASIGNATURA AS "Código Asignatura", 
    ASIG.NOMBRE_ASIGNATURA AS "Nombre Asignatura", 
    DOCS.NOMBRE_DOCENTE AS "Nombre Docente",
    DOCS.EMAIL_DOCENTE AS "Email Docente"
FROM ASIGNATURAS ASIG
JOIN DOCENTES DOCS ON ASIG.ID_DOCENTE = DOCS.ID;




