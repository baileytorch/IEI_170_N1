CREATE TABLE IF NOT EXISTS opciones_menu(
    id_opcion_menu INT AUTO_INCREMENT,
    opcion_menu VARCHAR(250) NOT NULL,
    numero_opcion INT NOT NULL,
    tipo_menu INT NOT NULL,
    
    CONSTRAINT pk_opciones_menu PRIMARY KEY (id_opcion_menu)
);