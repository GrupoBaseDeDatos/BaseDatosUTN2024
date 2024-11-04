-- Insertar datos iniciales en la tabla Proyectos
INSERT INTO Proyectos (NombreProyecto, RecursosNecesarios, Estado)
VALUES 
    ('Proyecto Alpha', 10, 'Pendiente'),
    ('Proyecto Beta', 5, 'Pendiente'),
    ('Proyecto Gamma', 15, 'Pendiente'),
    ('Proyecto Delta', 8, 'Pendiente'),
    ('Proyecto Epsilon', 3, 'Pendiente');

-- Insertar datos iniciales en la tabla RecursosDisponibles
INSERT INTO RecursosDisponibles (TipoRecurso, CantidadDisponible)
VALUES
    ('Recurso A', 20),
    ('Recurso B', 10),
    ('Recurso C', 5);
