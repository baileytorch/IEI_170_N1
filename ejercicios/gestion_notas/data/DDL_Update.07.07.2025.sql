USE 'gestion_notas';

ALTER TABLE asignaturas DROP FOREIGN KEY id_docente;

CREATE TABLE IF NOT EXISTS docentes_asignaturas(
    id_docente_asignatura INT AUTO_INCREMENT,
    id_docente INT NOT NULL,
    id_asignatura INT NOT NULL,

    CONSTRAINT pk_docentes_asignaturas PRIMARY KEY (id_docente_asignatura),
    CONSTRAINT fk_tabla_docentes FOREIGN KEY (id_docente) REFERENCES docentes (id_docente),
    CONSTRAINT fk_tabla_asignaturas FOREIGN KEY (id_asignatura) REFERENCES asignaturas (id_asignatura)
)