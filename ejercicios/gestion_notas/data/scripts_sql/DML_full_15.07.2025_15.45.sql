INSERT INTO docentes (nombre_docente,rut_docente,digito_verificador) VALUES 
('Aquiles Baeza',12345678,'5'),
('Wendy Sulca',13630677,'4'),
('Erick Bailey',12824290,'2');

INSERT INTO ASIGNATURAS (codigo_asignatura,nombre_asignatura) VALUES 
('BIO','Biología Celular'),
('QUI','Química Orgánica'),
('FIS','Cinemática');

INSERT INTO opciones_menu (opcion_menu,numero_opcion,tipo_menu) VALUES
('Gestión Asignaturas',1,1),
('Gestión Docentes',2,1),
('Salir',0,1),
('Listado Asignaturas',1,2),
('Agregar Asignatura',2,2),
('Editar Asignatura',3,2),
('Eliminar Asignatura',4,2),
('Volver',0,2),
('Listado Docentes',1,3),
('Agregar Docente',2,3),
('Editar Docente',3,3),
('Eliminar Docente',4,3),
('Volver',0,3);