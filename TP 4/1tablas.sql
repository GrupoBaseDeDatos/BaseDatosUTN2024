CREATE TABLE Proyectos (
    ProyectoId INT PRIMARY KEY IDENTITY(1,1),
    NombreProyecto VARCHAR(100) NOT NULL,
    RecursosNecesarios INT NOT NULL,
    RecursosAsignados INT DEFAULT 0,
    Estado VARCHAR(20) NOT NULL -- Ejemplos: 'Pendiente', 'En Curso', 'Completado'
);

CREATE TABLE RecursosDisponibles (
    RecursoId INT PRIMARY KEY IDENTITY(1,1),
    TipoRecurso VARCHAR(50) NOT NULL,
    CantidadDisponible INT NOT NULL
);
