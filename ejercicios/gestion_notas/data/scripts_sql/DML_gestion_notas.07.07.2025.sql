USE 'gestion_notas';

INSERT INTO docentes (nombre_docente,rut_docente,digito_verificador) VALUES 
('Aquiles Baeza',12345678,'5'),
('Wendy Sulca',13630677,'4'),
('Erick Bailey',12824290,'2');

INSERT INTO ASIGNATURAS (codigo_asignatura,nombre_asignatura) VALUES 
('BIO','Biología Celular'),
('QUI','Química Orgánica'),
('FIS','Cinemática');

SELECT * FROM DOCENTES;
SELECT * FROM ASIGNATURAS;