CREATE TABLE Proyectos (
    ProyectoId INT AUTO_INCREMENT PRIMARY KEY,
    NombreProyecto VARCHAR(100) NOT NULL,
    RecursosNecesarios INT NOT NULL,
    RecursosAsignados INT DEFAULT 0,
    Estado VARCHAR(20) NOT NULL
);

CREATE TABLE RecursosDisponibles (
    RecursoId INT AUTO_INCREMENT PRIMARY KEY,
    TipoRecurso VARCHAR(50) NOT NULL,
    CantidadDisponible INT NOT NULL
);

CREATE TABLE ProyectosRecursos (
    ProyectoRecursoId INT AUTO_INCREMENT PRIMARY KEY,
    ProyectoId INT,
    RecursoId INT,
    CantidadAsignada INT NOT NULL,
    FOREIGN KEY (ProyectoId) REFERENCES Proyectos(ProyectoId),
    FOREIGN KEY (RecursoId) REFERENCES RecursosDisponibles(RecursoId)
);
