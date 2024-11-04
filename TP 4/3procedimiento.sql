DELIMITER //
CREATE PROCEDURE AsignarRecursosAProyectos()
BEGIN
    DECLARE pId INT;
    DECLARE reqNecesarios INT;
    DECLARE estadoActual VARCHAR(20);
    DECLARE terminado INT DEFAULT FALSE;

    -- Definir cursor para proyectos pendientes
    DECLARE cursor_pendientes CURSOR FOR
        SELECT ProyectoId, RecursosNecesarios, Estado
        FROM Proyectos
        WHERE Estado = 'Pendiente'
        ORDER BY RecursosNecesarios DESC;

    -- Manejar fin del cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET terminado = TRUE;

    -- Iniciar el cursor
    OPEN cursor_pendientes;

    -- Procesar cada proyecto pendiente
    FETCH cursor_pendientes INTO pId, reqNecesarios, estadoActual;

    WHILE NOT terminado DO
        BEGIN
            DECLARE totalRecursos INT;

            -- Calcular la cantidad total de recursos disponibles
            SELECT SUM(CantidadDisponible) INTO totalRecursos
            FROM RecursosDisponibles;

            IF totalRecursos >= reqNecesarios THEN
                -- Actualizar el proyecto con los recursos asignados
                UPDATE Proyectos
                SET RecursosAsignados = reqNecesarios,
                    Estado = 'En Curso'
                WHERE ProyectoId = pId;

                -- Reducir los recursos disponibles
                UPDATE RecursosDisponibles
                SET CantidadDisponible = CantidadDisponible - reqNecesarios
                WHERE CantidadDisponible >= reqNecesarios
                LIMIT 1;
            END IF;

            -- Obtener el siguiente proyecto
            FETCH cursor_pendientes INTO pId, reqNecesarios, estadoActual;
        END;
    END WHILE;

    -- Cerrar el cursor
    CLOSE cursor_pendientes;
END//
DELIMITER ;
