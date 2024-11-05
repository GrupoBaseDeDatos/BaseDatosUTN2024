INSERT INTO Proyectos (NombreProyecto, RecursosNecesarios, RecursosAsignados, Estado) VALUES
('Desarrollo de Plataforma Web', 50, 20, 'En Curso'),
('Implementación de CRM', 30, 10, 'Pendiente'),
('Actualización de Servidores', 40, 40, 'Completado'),
('Optimización de Base de Datos', 20, 5, 'En Curso');

INSERT INTO RecursosDisponibles (TipoRecurso, CantidadDisponible) VALUES
('Desarrollador Web', 10),
('Analista de Sistemas', 5),
('Administrador de Servidores', 8),
('Especialista en Base de Datos', 7);

INSERT INTO ProyectosRecursos (ProyectoId, RecursoId, CantidadAsignada) VALUES
(1, 1, 5), 
(1, 2, 3), 
(2, 2, 2),  
(3, 3, 4), 
(4, 4, 2);  
