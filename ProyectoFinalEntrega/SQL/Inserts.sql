-- Insertar usuarios iniciales
INSERT INTO Usuarios (nombre, direccion, telefono, email, fecha_registro, cuota_mensual) VALUES
('Juan Pérez', 'Calle Ficticia 123', '123456789', 'juan@correo.com', '2023-02-15', 15.00),
('Ana Gómez', 'Avenida Siempre Viva 456', '987654321', 'ana@correo.com', '2023-06-20', 15.00),
('Luis Martínez', 'Calle Real 789', '112233445', 'luis@correo.com', '2023-01-10', 15.00),
('Maria López', 'Calle Falsa 101', '667788990', 'maria@correo.com', '2023-08-25', 15.00),
('Carlos Pérez', 'Avenida Libertador 202', '556677889', 'carlos@correo.com', '2023-03-15', 15.00),
('Sofia Díaz', 'Calle 12 de Octubre 303', '778899667', 'sofia@correo.com', '2023-04-10', 15.00),
('José Rodríguez', 'Calle Mayor 404', '334455667', 'jose@correo.com', '2023-07-22', 15.00),
('Laura Fernández', 'Avenida de los Álamos 505', '445566778', 'laura@correo.com', '2023-02-28', 15.00),
('Pedro Sánchez', 'Calle Larga 606', '556677889', 'pedro@correo.com', '2023-09-05', 15.00),
('Ana Martín', 'Avenida 9 de Julio 707', '998877665', 'ana.m@correo.com', '2023-01-15', 15.00);

-- Insertar libros iniciales
INSERT INTO Libros (titulo, autor, año_publicacion, isbn, disponible) VALUES
('El Quijote', 'Miguel de Cervantes', 1605, '978-3-16-148410-0', TRUE),
('Cien años de soledad', 'Gabriel García Márquez', 1967, '978-3-16-148411-7', TRUE),
('1984', 'George Orwell', 1949, '978-0-452-28423-4', TRUE),
('Matar a un ruiseñor', 'Harper Lee', 1960, '978-0-06-112008-4', TRUE),
('Don Juan Tenorio', 'Tirso de Molina', 1630, '978-84-376-0494-4', TRUE),
('Crimen y castigo', 'Fiódor Dostoyevski', 1866, '978-3-16-148412-4', TRUE),
('La sombra del viento', 'Carlos Ruiz Zafón', 2001, '978-84-670-1784-1', TRUE),
('Orgullo y prejuicio', 'Jane Austen', 1813, '978-0-14-143951-8', TRUE),
('La casa de los espíritus', 'Isabel Allende', 1982, '978-84-253-2907-4', TRUE),
('Ulises', 'James Joyce', 1922, '978-1-56459-763-7', TRUE);

-- Insertar préstamos iniciales
INSERT INTO Prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion) VALUES
(1, 3, '2024-02-01', '2024-02-15'),
(2, 1, '2024-02-03', '2024-02-17'),
(3, 2, '2024-02-10', '2024-02-24'),
(4, 5, '2024-02-12', '2024-02-26'),
(5, 4, '2024-02-15', '2024-02-29');

-- Insertar pagos iniciales
INSERT INTO Pagos (id_usuario, fecha_pago, monto) VALUES
(1, '2024-02-08', 15.00),
(2, '2024-02-05', 15.00),
(3, '2024-02-21', 15.00),
(4, '2024-02-12', 15.00),
(5, '2024-02-15', 15.00);